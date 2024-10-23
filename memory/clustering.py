
import numpy as np
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

def perform_clustering(memories, n_clusters=5):
    """
    Perform K-means clustering on memory data and return the clusters.
    """
    model = KMeans(n_clusters=n_clusters)
    clusters = model.fit_predict(memories)
    score = silhouette_score(memories, clusters)
    return clusters, score

def perform_dbscan_clustering(memories, eps=0.5, min_samples=5):
    """
    Perform DBSCAN clustering and return clusters and their scores.
    """
    model = DBSCAN(eps=eps, min_samples=min_samples)
    clusters = model.fit_predict(memories)
    return clusters

def perform_pca(memories, n_components=2):
    """
    Reduce memory dimensionality using PCA for better cluster visualization.
    """
    pca = PCA(n_components=n_components)
    reduced_memories = pca.fit_transform(memories)
    return reduced_memories
