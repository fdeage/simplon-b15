from sklearn.cluster import DBSCAN, AgglomerativeClustering, KMeans
from sklearn.metrics import silhouette_score


def score_dbscan(df):
    clustering = DBSCAN(eps=12.5, min_samples=4).fit(df)
    df["cluster"] = clustering.labels_

    return silhouette_score(df, clustering.labels_)


def score_agglo(df):
    clustering = AgglomerativeClustering(n_clusters=3).fit(df)
    df["cluster"] = clustering.labels_

    return silhouette_score(df, clustering.labels_)


def score_kmeans(df):
    clustering = KMeans(n_clusters=5).fit(df)
    df["cluster"] = clustering.labels_

    return silhouette_score(df, clustering.labels_)
