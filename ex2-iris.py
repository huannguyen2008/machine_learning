import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from mpl_toolkits import mplot3d

df = pd.read_csv('iris.data', names=['sepal length', 'sepal width', 'petal length', 'petal width', 'class'])
attributes = ['sepal length', 'sepal width', 'petal length', 'petal width']

# mean of the data
mean_vec = df.mean().values

# adjust the data to the center of the gravity
x = df.loc[:, attributes].values
y = df.loc[:, ['class']].values
data_adj = x - mean_vec
# print(data_adj)

# # calculate the covariance matrix
# cov_matrix = np.cov(data_adj, rowvar=False)
#
# # # eigenvectors and eigenvalues for the covariance matrix
# eig_val, eig_vec = np.linalg.eig(cov_matrix)

pca = PCA(n_components=3)
principal_comp = pca.fit_transform(data_adj)
principal_df = pd.DataFrame(data=principal_comp
                            , columns=['PC1', 'PC2', 'PC3'])

finalDf = pd.concat([principal_df, df[['class']]], axis=1)

targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
colors = ['r', 'g', 'b']
ax = plt.axes(projection='3d')
for target, color in zip(targets, colors):
    indicesToKeep = finalDf['class'] == target
    ax.scatter3D(finalDf.loc[indicesToKeep, 'PC1']
                 , finalDf.loc[indicesToKeep, 'PC2']
                 , finalDf.loc[indicesToKeep, 'PC3']
                 , c=color
                 , s=50)
plt.legend(targets)
plt.show()
print(pca.explained_variance_ratio_)
expected = [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1,1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]
 print(len(expected))