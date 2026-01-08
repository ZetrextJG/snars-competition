# SNARS community detection competition

## Method

Ward agglomerative clustering on the logarithmic Communicability matrix.

## Motivation

The idea for the clustering came from the biorxiv preprint "Extensive Benchmarking of Community Detection Algorithms" [1] which mentioned an algorithm called `blue_genes` which seems to outperform other methods considered in the paper on the gene expression data. The paper however is not particularly thorough in the description of the method, mentioning only that the clustering in done using Laplacian exponential diffusion kernels.

After a bit of searching I found the paper "Do logarithmic proximity measures outperform plain ones in graph clustering?" [2] which mentions a procedure similar to the one described as `blue_genes`. The paper analyses the difference between using "plain" node proximity measures and their logarithmic variants. On of the proximity measures used there was the exponential diffusion kernel $K_t = \exp(tA)$ [3], where $A$ is the adjacency matrix. Which after taking the element-wise logarithm seems to be a very effective similarity measure for community detection. (This differs from the Laplacian exponential diffusion kernel, but seems to perform better).

## Citations

[1] Sapna, R., Karthik, H., & Raman, K. (2025). Extensive Benchmarking of Community Detection Algorithms. bioRxiv, 2025-05.

[2] Ivashkin, V., & Chebotarev, P. (2016, May). Do logarithmic proximity measures outperform plain ones in graph clustering?. In International Conference on Network Analysis (pp. 87-105). Cham: Springer International Publishing.

[3] Estrada, E. (2012). The communicability distance in graphs. Linear Algebra and its Applications, 436(11), 4317-4328.