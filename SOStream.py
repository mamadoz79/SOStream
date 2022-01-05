from math import sqrt
import numpy as np
from math import inf

def dist(v1, v2):
    return np.sqrt(((v1 - v2) ** 2).sum())
  
def min_dist(vt, micro_clusters):
    micro_cluster_min_dist = inf
    min_micro_cluster = None
    for micro_cluster in micro_clusters:
        dist_to_micro_cluster = dist(vt, micro_cluster.centroid)
        if dist_to_micro_cluster <= micro_cluster_min_dist:
            micro_cluster_min_dist = dist_to_micro_cluster
            min_micro_cluster = micro_cluster
    return min_micro_cluster

  
  
class SOStream:
    def __init__(self):
        self.alpha = 0.3
        self.min_pts = 3
        self.M = [[]]
        self.merge_threshold = 3

    def process(self, vt):
        winner_cluster = min_dist(vt, self.M[-1])
        new_M = self.M[-1][:]
        if len(new_M) >= self.min_pts:
            winner_neighborhood = find_neighbors(winner_cluster, self.min_pts, new_M)
            if dist(vt, winner_cluster.centroid) < winner_cluster.radius:
                updateCluster(winner_cluster, vt, self.alpha, winner_neighborhood)
            else:
                new_M.append(newCluster(vt))
            overlap = find_overlap(winner_cluster, winner_neighborhood)
            if len(overlap) > 0:
                merged_cluster, deleted_clusters = merge_clusters(winner_cluster, overlap, self.merge_threshold)
                for deleted_cluster in deleted_clusters:
                    new_M.remove(deleted_cluster)
                if merged_cluster:
                    new_M.append(merged_cluster)
        else:
            new_M.append(newCluster(vt))

        self.M.append(new_M)
