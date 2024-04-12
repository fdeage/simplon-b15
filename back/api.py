from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

import method_kmeans as kmeans
import method_dbscan as dbscan
import method_hierarchical as hierarchical

from processing import get_data


def handle_cors(app):
    # allow everything, yeah!
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app


app = handle_cors(FastAPI())


@app.get("/list_methods", description="List clustering methods")
async def list_methods():
    methods = ["k_means", "dbscan", "hierarchical"]
    return {"methods": methods}


@app.get("/methods/{method_name}/score")
def get_method_score(method_name: str):
    df = get_data()

    if method_name == "k_means":
        score = kmeans.compute_score(df)
        return {"resp": "ok", "data": {"score": score}}

    elif method_name == "dbscan":
        score = dbscan.compute_score(df)
        return {"resp": "ok", "data": {"score": score}}

    elif method_name == "hierarchical":
        score = hierarchical.compute_score(df)
        return {"resp": "ok", "data": {"score": score}}

    else:
        return {"message": f"No method {method_name}"}


@app.post("/methods/{method_name}/retrain")
def retrain_method(method_name: str):
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
