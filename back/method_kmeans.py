from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def compute_score(df):
    clustering = KMeans(n_clusters=5).fit(df)
    df['cluster'] = clustering.labels_

    return silhouette_score(df, clustering.labels_)
