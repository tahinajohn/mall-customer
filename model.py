import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

dataset = pd.read_csv("datasets/Mall_Customers.csv")
dataset = dataset.drop("CustomerID", axis=1)

X = dataset.iloc[:, [2, 3]].values

kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 42, n_init="auto")
y_kmeans = kmeans.fit_predict(X)