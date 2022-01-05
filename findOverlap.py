from math import sqrt
import numpy as np

def dist(v1, v2):
    return np.sqrt(((v1 - v2) ** 2).sum())
  
def find_overlap(win, win_n):
  overlap = []
  for n_i in win_n:
    if win is not n_i:
      if dist(win.centroid, n_i.centroid) - (win.radius + n_i.radius) < 0 :
        overlap.append(n_i)
  return overlap
