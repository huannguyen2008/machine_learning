import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA

fish_data = pd.read_csv('qsar_fish_toxicity.csv', sep=';',
                        names=['CIC0', 'SM1_Dz(Z)', 'GATS1i', 'NdsCH', 'NdssC', 'MLOGP',
                               'quantitative response, LC50 [-LOG(mol/L)]'])
attributes = ['CIC0', 'SM1_Dz(Z)', 'GATS1i', 'NdsCH', 'NdssC', 'MLOGP']
# mean of the data

# adjust the data to the center of the gravity
x = fish_data.loc[:, attributes].values
mean_vec = np.mean(x)
y = fish_data.loc[:, ['quantitative response, LC50 [-LOG(mol/L)]']].values
data_adj = x - mean_vec

pca = PCA(n_components=2)
principal_comp = pca.fit_transform(data_adj)
principal_df = pd.DataFrame(data=principal_comp
                            , columns=['PC1', 'PC2'])

finalDf = pd.concat([principal_df, fish_data[['quantitative response, LC50 [-LOG(mol/L)]']]], axis=1)

targets = []
for i in len(fish_data[['quantitative response, LC50 [-LOG(mol/L)]']])
colors = ['r']
for target, color in zip(targets, colors):
    indicesToKeep = finalDf['quantitative response, LC50 [-LOG(mol/L)]'] == target
    plt.scatter(finalDf.loc[indicesToKeep, 'PC1']
                , finalDf.loc[indicesToKeep, 'PC2']
                , c=color
                , s=50)

plt.legend(targets)
plt.show()
