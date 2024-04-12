from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score

def compute_score(df):
    clustering = DBSCAN(eps=12.5, min_samples=4).fit(df)
    df['cluster'] = clustering.labels_

    return silhouette_score(df, clustering.labels_)
