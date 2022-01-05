from math import exp
def updateCluster(win_cluster, vt, alpha, winner_nn):
    win_cluster.centroid = (win_cluster.number_points * win_cluster.centroid + vt) / (win_cluster.number_points+1)
    win_cluster.number_points += 1
    width_neighbor = win_cluster.radius ** 2
    for neighbor_cluster in winner_nn:
        beta = exp(-(dist(neighbor_cluster.centroid, win_cluster.centroid)/(2 * width_neighbor)))
        neighbor_cluster.centroid = neighbor_cluster.centroid + alpha*bata*(win_cluster.centroid-neighbor_cluster.centroid)
