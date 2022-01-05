from math import sqrt
import numpy as np

def dist(v1, v2):
    return np.sqrt(((v1 - v2) ** 2).sum())

def find_neighbors(win_cluster, min_pts, M_t):
  if len(M_t) >= min_pts:
    win_dist = []
    for microcluster in M_t:
      win_dist.append(dist(microcluster.centroid, win_cluster.centroid))
    win_dist.sort()
    k_dist = win_dist[min_pts-1]
    win_cluster.radius = k_dist
    win_nn = []
    for i in win_dist:
      if i[1] <= k_dist:
        win_nn.append(M_t[d[0]])
    return win_nn
  else:
    return []
