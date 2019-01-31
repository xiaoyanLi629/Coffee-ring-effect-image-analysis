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
Data_1 = np.loadtxt(open('1_total_properties_0.95_6.csv', 'rb'), delimiter=",", skiprows=1)
Data_1 = preprocessing.scale(Data_1, with_std = False)

numComponents = 3
pca = PCA(n_components=numComponents)
pca.fit(Data_1)
Data_trans_1 = pca.transform(Data_1)

# Data 2
Data_2 = np.loadtxt(open('2_total_properties_0.89_11.csv', 'rb'), delimiter=",", skiprows=1)
Data_2 = preprocessing.scale(Data_2, with_std = False)

numComponents = 3
pca = PCA(n_components=numComponents)
pca.fit(Data_2)
Data_trans_2 = pca.transform(Data_2)

# Data 3
Data_3 = np.loadtxt(open('3_total_properties_0.86_4.csv', 'rb'), delimiter=",", skiprows=1)
Data_3 = preprocessing.scale(Data_3, with_std = False)

numComponents = 3
pca = PCA(n_components=numComponents)
pca.fit(Data_3)
Data_trans_3 = pca.transform(Data_3)


# Data 4
Data_4 = np.loadtxt(open('4_total_properties_0.93_6.csv', 'rb'), delimiter=",", skiprows=1)
Data_4 = preprocessing.scale(Data_4, with_std = False)

numComponents = 3
pca = PCA(n_components=numComponents)
pca.fit(Data_4)
Data_trans_4 = pca.transform(Data_4)

# 2d image
# plot
fig, axarr = plt.subplots(2, 2)
axarr[0, 0].scatter(Data_trans_1[0:5, 0], Data_trans_1[0:5, 1], c = 'r', s = 25, marker = 'x', label = '$NaCl\; 10mM,\; CaCl_2\; 3.0mM,\; MgCl_2\; 1.5mM$')
axarr[0, 0].scatter(Data_trans_1[5:10, 0], Data_trans_1[5:10, 1], c = 'g', s = 25, marker = 'x', label = '$NaCl\; 5.0mM,\; CaCl_2\; 3.0mM,\; MgCl_2\; 1.5mM$')
axarr[0, 0].scatter(Data_trans_1[10:15, 0], Data_trans_1[10:15, 1], c = 'b', s = 25, marker = 'x', label = '$NaCl\; 2.5mM,\; CaCl_2\; 3.0mM,\; MgCl_2\; 1.5mM$')

axarr[0, 1].scatter(Data_trans_2[0:5, 0], Data_trans_2[0:5, 1], c = 'r', s = 25, marker = 'x', label = '$NaHCO_3\; 10mM,\; CaCl_2\; 0.5mM,\; MgCl_2\; 0.25mM$')
axarr[0, 1].scatter(Data_trans_2[5:10, 0], Data_trans_2[5:10, 1], c = 'g', s = 25, marker = 'x', label = '$NaHCO_3\; 5.0mM,\; CaCl_2\; 0.5mM,\; MgCl_2\; 0.25mM$')
axarr[0, 1].scatter(Data_trans_2[10:15, 0], Data_trans_2[10:15, 1], c = 'b', s = 25, marker = 'x', label = '$NaHCO_3\; 2.5mM,\; CaCl_2\; 0.5mM,\; MgCl_2\; 0.25mM$')

axarr[1, 0].scatter(Data_trans_3[0:5, 0], Data_trans_3[0:5, 1], c = 'r', s = 25, marker = 'x', label = '$Na_2SO_4\; 10mM,\; CaSO_4\; 0.5mM,\; MgSO_4\; 0.25mM$')
axarr[1, 0].scatter(Data_trans_3[5:10, 0], Data_trans_3[5:10, 1], c = 'g', s = 25, marker = 'x', label = '$Na_2SO_4\; 5.0mM,\; CaSO_4\; 0.5mM,\; MgSO_4\; 0.25mM$')
axarr[1, 0].scatter(Data_trans_3[10:15, 0], Data_trans_3[10:15, 1], c = 'b', s = 25, marker = 'x', label = '$Na_2SO_4\; 2.5mM,\; CaSO_4\; 0.5mM,\; MgSO_4\; 0.25mM$')

axarr[1, 1].scatter(Data_trans_4[0:5, 0], Data_trans_4[0:5, 1], c = 'r', s = 25, marker = 'x', label = '$NaHCO_3\; 10mM,\; CaSO_4\; 0.5mM,\; MgSO_4\; 0.25mM$')
axarr[1, 1].scatter(Data_trans_4[5:10, 0], Data_trans_4[5:10, 1], c = 'g', s = 25, marker = 'x', label = '$NaHCO_3\; 5.0mM,\; CaSO_4\; 0.5mM,\; MgSO_4\; 0.25mM$')
axarr[1, 1].scatter(Data_trans_4[10:15, 0], Data_trans_4[10:15, 1], c = 'b', s = 25, marker = 'x', label = '$NaHCO_3\; 2.5mM,\; CaSO_4\; 0.5mM,\; MgSO_4\; 0.25mM$')

axarr[0, 0].set_title('$NaCl\; CaCl_2\; MgCl_2$')
axarr[0, 1].set_title('$NaHCO_3\; CaCl_2\; MgCl_2$')
axarr[1, 0].set_title('$Na_2SO_4\; CaSO_4\; MgSO_4$')
axarr[1, 1].set_title('$NaHCO_3\; CaSO_4\; MgSO_4$')

axarr[0, 0].set_yticklabels([])
axarr[0, 0].set_xticklabels([])
axarr[0, 1].set_yticklabels([])
axarr[0, 1].set_xticklabels([])
axarr[1, 0].set_yticklabels([])
axarr[1, 0].set_xticklabels([])
axarr[1, 1].set_yticklabels([])
axarr[1, 1].set_xticklabels([])

axarr[0, 0].legend(loc = 'upper right', prop={'size': 5}, labelspacing = 0, handletextpad = 0)
axarr[0, 1].legend(loc = 'upper right', prop={'size': 5}, labelspacing = 0, handletextpad = 0)
axarr[1, 0].legend(loc = 'upper right', prop={'size': 5}, labelspacing = 0, handletextpad = 0)
axarr[1, 1].legend(loc = 'upper right', prop={'size': 5}, labelspacing = 0, handletextpad = 0)

for ax in axarr.flat:
    ax.set(xlabel='PC-1', ylabel='PC-2')
for ax in axarr.flat:
    ax.label_outer()
plt.tight_layout()

fig.savefig('PCA_chemistry_2d_4_subplots.jpg', dpi = 1000)
# plt.show()
