import numpy as np
from scipy.linalg import expm
import scipy.cluster.hierarchy as sch

def log_diffusion_similarity(adj_matrix, t = 0.54):
    exp_L = expm(t * adj_matrix)
    log_exp_L = np.log(exp_L)
    return log_exp_L

def get_clustering(adj_matrix, t = 0.54):
    clustering = sch.ward(log_diffusion_similarity(adj_matrix, t))
    return clustering
