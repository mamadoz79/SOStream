from math import sqrt
import numpy as np

def mean(a, b, wieght_a, wieght_b):
    return ((wieght_a * a + wieght_b * b)/(wieght_a + wieght_b))

def dist(v1, v2):
    return np.sqrt(((v1 - v2) ** 2).sum())

def merge_clusters(win_cluster, overlaping_clusters):
    merged_cluster = None
    deleted_clusters = []
    for cluster in overlaping_clusters:
      if len(deleted_clusters) == 0:
          deleted_clusters.append(win_cluster)
          merged_cluster = MicroCluster(win_cluster.centroid, number_points=win_cluster.number_points, radius=win_cluster.radius)
      merged_cluster = merge(cluster, merged_cluster)
      deleted_clusters.append(cluster)
    return merged_cluster, deleted_clusters
  
def merge(cluster_a, cluster_b):
  new_cluster_centroid = mean(cluster_a.centroid, cluster_b.centroid, cluster_a.number_points, cluster_b.number_points)
  new_cluster_radius = dist(cluster_a.centroid, cluster_b.centroid) + max(cluster_a.radius, cluster_b.radius)
  new_cluster = MicroCluster(centroid=new_cluster_centroid, number_points=cluster_a.number_points + cluster_b.number_points, radius=new_cluster_radius)
  return new_cluster
