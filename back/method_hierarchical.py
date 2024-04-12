from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score

def compute_score(df):
    clustering = AgglomerativeClustering(n_clusters=3).fit(df)
    df['cluster'] = clustering.labels_

    return silhouette_score(df, clustering.labels_)
