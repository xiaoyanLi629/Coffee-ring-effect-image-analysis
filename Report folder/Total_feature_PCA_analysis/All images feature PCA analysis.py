import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import pandas as pd
from sklearn.decomposition import PCA
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.linalg import eigs
import csv
from sklearn import preprocessing

# Data 1
Data = np.loadtxt(open('total_feature_data.csv', 'rb'), delimiter=",", skiprows=1)
Data = preprocessing.scale(Data, with_std = False)

numComponents = 3
pca = PCA(n_components=numComponents)
pca.fit(Data)
Data_trans = pca.transform(Data)

# 2d image
# plot
fig, ax = plt.subplots(1, 1)

ax.scatter(Data_trans[0:5, 0], Data_trans[0:5, 1], s = 25,  marker = 'x', c = 'r', label = '$NaCl\; 10mM,\; CaCl_2\; 3.0mM,\; MgCl_2\; 1.5mM$')
ax.scatter(Data_trans[5:10, 0], Data_trans[5:10, 1], s = 25, marker = 'o', facecolors = 'none', edgecolors='r',
           label = '$NaCl\; 5.0mM,\; CaCl_2\; 3.0mM,\; MgCl_2\; 1.5mM$')
ax.scatter(Data_trans[10:15, 0], Data_trans[10:15, 1], s = 25, marker = 's', facecolors = 'none', edgecolors='r',
           label =  '$NaCl\; 2.5mM,\; CaCl_2\; 3.0mM,\; MgCl_2\; 1.5mM$')

ax.scatter(Data_trans[15:20, 0], Data_trans[15:20, 1], s = 25, marker = 'x', c = 'g', label = '$NaHCO_3\; 10mM,\; CaCl_2\; 0.5mM,\; MgCl_2\; 0.25mM$')
ax.scatter(Data_trans[20:25, 0], Data_trans[20:25, 1], s = 25, marker = 'o', facecolors = 'none', edgecolors='g',
           label = '$NaHCO_3\; 5.0mM,\; CaCl_2\; 0.5mM,\; MgCl_2\; 0.25mM$')
ax.scatter(Data_trans[25:30, 0], Data_trans[25:30, 1], s = 25, marker = 's', facecolors = 'none', edgecolors='g',
           label = '$NaHCO_3\; 2.5mM,\; CaCl_2\; 0.5mM,\; MgCl_2\; 0.25mM$')

ax.scatter(Data_trans[30:35, 0], Data_trans[30:35, 1], s = 25, marker = 'x', c = 'b', label = '$Na_2SO_4\; 10mM,\; CaSO_4\; 0.5mM,\; MgSO_4\; 0.25mM$')
ax.scatter(Data_trans[35:40, 0], Data_trans[35:40, 1], s = 25, marker = 'o', facecolors = 'none', edgecolors='b',
           label = '$Na_2SO_4\; 5.0mM,\; CaSO_4\; 0.5mM,\; MgSO_4\; 0.25mM$')
ax.scatter(Data_trans[40:45, 0], Data_trans[40:45, 1], s = 25, marker = 's', facecolors = 'none', edgecolors='b',
           label = '$Na_2SO_4\; 2.5mM,\; CaSO_4\; 0.5mM,\; MgSO_4\; 0.25mM$')

ax.scatter(Data_trans[45:50, 0], Data_trans[45:50, 1], s = 25, marker = 'x', c = 'y', label = '$NaHCO_3\; 10mM,\; CaSO_4\; 0.5mM,\; MgSO_4\; 0.25mM$')
ax.scatter(Data_trans[50:55, 0], Data_trans[50:55, 1], s = 25, marker = 'o', facecolors = 'none', edgecolors='y',
           label = '$NaHCO_3\; 5.0mM,\; CaSO_4\; 0.5mM,\; MgSO_4\; 0.25mM$')
ax.scatter(Data_trans[55:60, 0], Data_trans[55:60, 1], s = 25, marker = 's', facecolors = 'none', edgecolors='y',
           label = '$NaHCO_3\; 2.5mM,\; CaSO_4\; 0.5mM,\; MgSO_4\; 0.25mM$')

plt.xlabel('First component')
plt.ylabel('Second component')
ax.set_yticklabels([])
ax.set_xticklabels([])

# plt.title('PCA Image analysis for all samples')
ax.legend(loc='upper right', prop={'size': 7}, handletextpad = 0, labelspacing = 0)
plt.show()
fig.savefig('PCA_all_images_features_2_comonents_1_plot.jpg', dpi = 1000)