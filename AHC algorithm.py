from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch

X = [[i] for i in [1, 2, 9, 12, 20]]

# df = pd.read_csv('iris.data', names=['sepal length', 'sepal width', 'petal length', 'petal width', 'class'])
# attributes = ['sepal length', 'sepal width']
#
# x = df.loc[:, attributes].values
# y = df.loc[:, ['class']].values


dendrogram = sch.dendrogram(sch.linkage(X, method='single'))
fig = plt.figure(figsize=(5, 10))
plt.show()


# Z = linkage(x, 'single')
# fig = plt.figure(figsize=(5, 10))
# dn = dendrogram(Z)
# plt.show()
