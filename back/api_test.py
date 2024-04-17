# Pas indispensable pour tester mais plus pratique que de simples `assert()`
from fastapi.testclient import TestClient

# On importe le `app = FastAPI()` défini dans le fichier que l'on teste
from api import app

client = TestClient(app)


def test_list_methods():
    response = client.get("/list_methods")

    assert response.status_code == 200
    assert response.json() == {"methods": ["k_means", "dbscan", "hierarchical"]}


test_list_methods()
