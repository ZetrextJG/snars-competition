import numpy as np
import scipy.cluster.hierarchy as sch
from impl import log_diffusion_similarity
from sklearn.metrics import silhouette_score
from kneed import KneeLocator
import time

# Filename, Number of clusters, Smoothing parameter t
COMPETITION_DATASETS = [
    ("D1-K=2.csv", 2, 0.54),
    ("D1-UNC.csv", None, 0.54),
    ("D2-K=7.csv", 7, 0.54),
    ("D2-UNC.csv", None, 0.54),
    ("D3-K=12.csv", 12, 0.54),
    ("D3-UNC.csv", None, 0.54),
]

def main():
    print("Hello from snars-competition!")

    for filename, K, t, _ in COMPETITION_DATASETS:
        print(f"Processing dataset: {filename} with t={t} and K={K}")
        adj_matrix = np.loadtxt(f"competition/{filename}", delimiter=",")
        N = adj_matrix.shape[0]

        start_time = time.time_ns()
        log_exp_L = log_diffusion_similarity(adj_matrix, t=t)
        clustering = sch.ward(log_exp_L)

        if K is None:
            silhouette_scores = []
            for n_clusters in range(2, 20):
                if n_clusters >= N:
                    break
                cluster_labels = sch.fcluster(clustering, t=n_clusters, criterion='maxclust')
                score = silhouette_score(log_exp_L, cluster_labels, metric='euclidean')
                silhouette_scores.append(score)

            kneedle = KneeLocator(range(2, 20), silhouette_scores, S=0.5, curve="concave", direction="increasing")
            K = kneedle.knee
            print(f"Determined optimal K: {K}")

        cluster_labels = sch.fcluster(clustering, t=K, criterion='maxclust')
        end_time = time.time_ns()

        # Save labels to 2 columns csv
        np.savetxt(f"labels/{filename}", 
                   np.column_stack((np.arange(N) + 1, cluster_labels)), 
                   delimiter=",", fmt='%d', comments='')

        print(f"Clustering completed in {(end_time - start_time) / 1e9:.4f} seconds.")
        print(f"Cluster labels: {len(np.unique(cluster_labels))}")



if __name__ == "__main__":
    main()
