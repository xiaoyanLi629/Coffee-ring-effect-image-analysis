import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image
import pandas as pd
from sklearn.decomposition import PCA
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.linalg import eigs
from mpl_toolkits.mplot3d import Axes3D

# Data_1
numImages = 15
Data_1 = np.zeros(shape = (numImages, 490*490))

for i in range(1, numImages + 1):
    filename = str(i)+'.jpg'
    img = mpimg.imread(filename)
    img = img[:, :, 0]*0.299 + img[:, :, 1]*0.587 + img[:, :, 2]*0.114
    Data_1[i-1] = np.array(img.flatten()).reshape(1, img.shape[0]*img.shape[1])

numComponents = 15
pca = PCA(n_components=numComponents)
pca.fit(Data_1)
Data_tran_1 = pca.transform(Data_1)

# Data_2
numImages = 15
Data_2 = np.zeros(shape = (numImages, 490*490))

for i in range(1, numImages + 1):
    filename = str(i+15)+'.jpg'
    img = mpimg.imread(filename)
    img = img[:, :, 0]*0.299 + img[:, :, 1]*0.587 + img[:, :, 2]*0.114
    Data_2[i-1] = np.array(img.flatten()).reshape(1, img.shape[0]*img.shape[1])

numComponents = 15
pca = PCA(n_components=numComponents)
pca.fit(Data_2)
Data_tran_2 = pca.transform(Data_2)

# Data_3
numImages = 15
Data_3 = np.zeros(shape = (numImages, 490*490))

for i in range(1, numImages + 1):
    filename = str(i+30)+'.jpg'
    img = mpimg.imread(filename)
    img = img[:, :, 0]*0.299 + img[:, :, 1]*0.587 + img[:, :, 2]*0.114
    Data_3[i-1] = np.array(img.flatten()).reshape(1, img.shape[0]*img.shape[1])

numComponents = 15
pca = PCA(n_components=numComponents)
pca.fit(Data_3)
Data_tran_3 = pca.transform(Data_3)

# Data_4
numImages = 15
Data_4 = np.zeros(shape = (numImages, 490*490))

for i in range(1, numImages + 1):
    filename = str(i+45)+'.jpg'
    img = mpimg.imread(filename)
    img = img[:, :, 0]*0.299 + img[:, :, 1]*0.587 + img[:, :, 2]*0.114
    Data_4[i-1] = np.array(img.flatten()).reshape(1, img.shape[0]*img.shape[1])

numComponents = 15
pca = PCA(n_components=numComponents)
pca.fit(Data_4)
Data_tran_4 = pca.transform(Data_4)

# plot
f, axarr = plt.subplots(2, 2)
axarr[0, 0].scatter(Data_tran_1[0:5, 0], Data_tran_1[0:5, 1], c = 'r', s = 25, marker = 'x', label = '$NaCl\; 10mM,\; CaCl_2\; 3.0mM,\; MgCl_2\; 1.5mM$')
axarr[0, 0].scatter(Data_tran_1[5:10, 0], Data_tran_1[5:10, 1], c = 'g', s = 25, marker = 'x', label = '$NaCl\; 5.0mM,\; CaCl_2\; 3.0mM,\; MgCl_2\; 1.5mM$')
axarr[0, 0].scatter(Data_tran_1[10:15, 0], Data_tran_1[10:15, 1], c = 'b', s = 25, marker = 'x', label = '$NaCl\; 2.5mM,\; CaCl_2\; 3.0mM,\; MgCl_2\; 1.5mM$')

axarr[0, 1].scatter(Data_tran_2[0:5, 0], Data_tran_2[0:5, 1], c = 'r', s = 25, marker = 'x', label = '$NaHCO_3\; 10mM,\; CaCl_2\; 0.5mM,\; MgCl_2\; 0.25mM$')
axarr[0, 1].scatter(Data_tran_2[5:10, 0], Data_tran_2[5:10, 1], c = 'g', s = 25, marker = 'x', label = '$NaHCO_3\; 5.0mM,\; CaCl_2\; 0.5mM,\; MgCl_2\; 0.25mM$')
axarr[0, 1].scatter(Data_tran_2[10:15, 0], Data_tran_2[10:15, 1], c = 'b', s = 25, marker = 'x', label = '$NaHCO_3\; 2.5mM,\; CaCl_2\; 0.5mM,\; MgCl_2\; 0.25mM$')

axarr[1, 0].scatter(Data_tran_3[0:5, 0], Data_tran_3[0:5, 1], c = 'r', s = 25, marker = 'x', label = '$Na_2SO_4\; 10mM,\; CaSO_4\; 0.5mM,\; MgSO_4\; 0.25mM$')
axarr[1, 0].scatter(Data_tran_3[5:10, 0], Data_tran_3[5:10, 1], c = 'g', s = 25, marker = 'x', label = '$Na_2SO_4\; 5.0mM,\; CaSO_4\; 0.5mM,\; MgSO_4\; 0.25mM$')
axarr[1, 0].scatter(Data_tran_3[10:15, 0], Data_tran_3[10:15, 1], c = 'b', s = 25, marker = 'x', label = '$Na_2SO_4\; 2.5mM,\; CaSO_4\; 0.5mM,\; MgSO_4\; 0.25mM$')

axarr[1, 1].scatter(Data_tran_4[0:5, 0], Data_tran_4[0:5, 1], c = 'r', s = 25, marker = 'x', label = '$NaHCO_3\; 10mM,\; CaSO_4\; 0.5mM,\; MgSO_4\; 0.25mM$')
axarr[1, 1].scatter(Data_tran_4[5:10, 0], Data_tran_4[5:10, 1], c = 'g', s = 25, marker = 'x', label = '$NaHCO_3\; 5.0mM,\; CaSO_4\; 0.5mM,\; MgSO_4\; 0.25mM$')
axarr[1, 1].scatter(Data_tran_4[10:15, 0], Data_tran_4[10:15, 1], c = 'b', s = 25, marker = 'x', label = '$NaHCO_3\; 2.5mM,\; CaSO_4\; 0.5mM,\; MgSO_4\; 0.25mM$')

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
plt.show()
f.savefig('PCA_image_2_components_4_subplots.jpg', dpi = 1000)

