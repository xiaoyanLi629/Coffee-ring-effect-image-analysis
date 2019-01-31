import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image
import pandas as pd
from sklearn.decomposition import PCA
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.linalg import eigs
from numpy import linalg as LA
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import figure


numImages = 60
# fig = plt.figure(figsize = (8,8))
X = np.zeros(shape = (numImages, 490*490))

for i in range(1, numImages + 1):
    filename = str(i)+'.jpg'
    img = mpimg.imread(filename)
    img = img[:, :, 0]*0.299 + img[:, :, 1]*0.587 + img[:, :, 2]*0.114
    X[i-1] = np.array(img.flatten()).reshape(1, img.shape[0]*img.shape[1])

numComponents = 60
pca = PCA(n_components=numComponents)

pca.fit(X)
Z = pca.transform(X)
fig1, ax = plt.subplots()

ax.scatter(Z[0:5, 0], Z[0:5, 1], s = 25,  marker = 'x', c = 'r', label = '$NaCl\; 10mM,\; CaCl_2\; 3.0mM,\; MgCl_2\; 1.5mM$')
ax.scatter(Z[5:10, 0], Z[5:10, 1], s = 25, marker = 'o', facecolors = 'none', edgecolors='r',
           label = '$NaCl\; 5.0mM,\; CaCl_2\; 3.0mM,\; MgCl_2\; 1.5mM$')
ax.scatter(Z[10:15, 0], Z[10:15, 1], s = 25, marker = 's', facecolors = 'none', edgecolors='r',
           label =  '$NaCl\; 2.5mM,\; CaCl_2\; 3.0mM,\; MgCl_2\; 1.5mM$')

ax.scatter(Z[15:20, 0], Z[15:20, 1], s = 25, marker = 'x', c = 'g', label = '$NaHCO_3\; 10mM,\; CaCl_2\; 0.5mM,\; MgCl_2\; 0.25mM$')
ax.scatter(Z[20:25, 0], Z[20:25, 1], s = 25, marker = 'o', facecolors = 'none', edgecolors='g',
           label = '$NaHCO_3\; 5.0mM,\; CaCl_2\; 0.5mM,\; MgCl_2\; 0.25mM$')
ax.scatter(Z[25:30, 0], Z[25:30, 1], s = 25, marker = 's', facecolors = 'none', edgecolors='g',
           label = '$NaHCO_3\; 2.5mM,\; CaCl_2\; 0.5mM,\; MgCl_2\; 0.25mM$')

ax.scatter(Z[30:35, 0], Z[30:35, 1], s = 25, marker = 'x', c = 'b', label = '$Na_2SO_4\; 10mM,\; CaSO_4\; 0.5mM,\; MgSO_4\; 0.25mM$')
ax.scatter(Z[35:40, 0], Z[35:40, 1], s = 25, marker = 'o', facecolors = 'none', edgecolors='b',
           label = '$Na_2SO_4\; 5.0mM,\; CaSO_4\; 0.5mM,\; MgSO_4\; 0.25mM$')
ax.scatter(Z[40:45, 0], Z[40:45, 1], s = 25, marker = 's', facecolors = 'none', edgecolors='b',
           label = '$Na_2SO_4\; 2.5mM,\; CaSO_4\; 0.5mM,\; MgSO_4\; 0.25mM$')

ax.scatter(Z[45:50, 0], Z[45:50, 1], s = 25, marker = 'x', c = 'y', label = '$NaHCO_3\; 10mM,\; CaSO_4\; 0.5mM,\; MgSO_4\; 0.25mM$')
ax.scatter(Z[50:55, 0], Z[50:55, 1], s = 25, marker = 'o', facecolors = 'none', edgecolors='y',
           label = '$NaHCO_3\; 5.0mM,\; CaSO_4\; 0.5mM,\; MgSO_4\; 0.25mM$')
ax.scatter(Z[55:60, 0], Z[55:60, 1], s = 25, marker = 's', facecolors = 'none', edgecolors='y',
           label = '$NaHCO_3\; 2.5mM,\; CaSO_4\; 0.5mM,\; MgSO_4\; 0.25mM$')

plt.xlabel('First component')
plt.ylabel('Second component')
ax.set_yticklabels([])
ax.set_xticklabels([])

# plt.title('PCA Image analysis for all samples')
ax.legend(loc='upper right', prop={'size': 7}, handletextpad = 0, labelspacing = 0)
plt.show()
fig1.savefig('PCA_all_images_2_components_1_plot.jpg', dpi = 1000)

# # use component 3 and 4
# fig2, ax = plt.subplots()
# ax.scatter(Z[0:5, 2], Z[0:5, 3], s = 100,  marker = 'x', c = 'r', label = 'NaCl 10mM, CaCl2 3.0mM, MgCl2 1.5mM')
# ax.scatter(Z[5:10, 2], Z[5:10, 3], s = 100, marker = 'o', facecolors = 'none', edgecolors='r',
#            label = 'NaCl 5.0mM, CaCl2 3.0mM, MgCl2 1.5mM')
# ax.scatter(Z[10:15, 2], Z[10:15, 3], s = 100, marker = 's', facecolors = 'none', edgecolors='r',
#            label =  'NaCl 2.5mM, CaCl2 3.0mM, MgCl2 1.5mM')
#
# ax.scatter(Z[15:20, 2], Z[15:20, 3], s = 100, marker = 'x', c = 'g', label = 'NaHCO3 10mM, CaCl2 0.5mM, MgCl2 0.25mM')
# ax.scatter(Z[20:25, 2], Z[20:25, 3], s = 100, marker = 'o', facecolors = 'none', edgecolors='g',
#            label = 'NaHCO3 5.0mM, CaCl2 0.5mM, MgCl2 0.25mM')
# ax.scatter(Z[25:30, 2], Z[25:30, 3], s = 100, marker = 's', facecolors = 'none', edgecolors='g',
#            label = 'NaHCO3 2.5mM, CaCl2 0.5mM, MgCl2 0.25mM')
#
# ax.scatter(Z[30:35, 2], Z[30:35, 3], s = 100, marker = 'x', c = 'b', label = 'Na2SO4 5.0mM, CaSO4 0.5mM, MgSO4 0.25mM')
# ax.scatter(Z[35:40, 2], Z[35:40, 3], s = 100, marker = 'o', facecolors = 'none', edgecolors='b',
#            label = 'Na2SO4 2.5mM, CaSO4 0.5mM, MgSO4 0.25mM')
# ax.scatter(Z[40:45, 2], Z[40:45, 3], s = 100, marker = 's', facecolors = 'none', edgecolors='b',
#            label='Na2SO4 1.25mM, CaSO4 0.5mM, MgSO4 0.25mM')
#
# ax.scatter(Z[45:50, 2], Z[45:50, 3], s = 100, marker = 'x', c = 'y', label = 'NaHCO3 10mM, CaSO4 0.5mM, MgSO4 0.25mM')
# ax.scatter(Z[50:55, 2], Z[50:55, 3], s = 100, marker = 'o', facecolors = 'none', edgecolors='y',
#            label = 'NaHCO3 5.0mM, CaSO4 0.5mM, MgSO4 0.25mM')
# ax.scatter(Z[55:60, 2], Z[55:60, 3], s = 100, marker = 's', facecolors = 'none', edgecolors='y',
#            label = 'NaHCO3 2.5mM, CaSO4 0.5mM, MgSO4 0.25mM')
#
# plt.xlabel('Third component', fontsize = 20)
# plt.ylabel('Fourth component', fontsize = 20)
# plt.title('PCA Image analysis for all samples', fontsize = 20)
# ax.legend(loc = 'upper right', prop={'size': 7})
# plt.show()

#
# eigenvalues = pca.explained_variance_
# variance = []
# for i in range(len(eigenvalues)):
#     if i == 0:
#         variance.append(eigenvalues[0])
#     else:
#         variance.append(variance[i-1] + eigenvalues[i])
# variance = variance/variance[-1]
#
# fig3, ax = plt.subplots()
# plt.plot(variance, 'ro-', linewidth=1)
# plt.title('Scree Plot for all 60 images', fontsize=20)
# plt.xlabel('Principal Component', fontsize=20)
# plt.ylabel('Cumulative Eigenvalue', fontsize=20)
# fig3.savefig('Scree Plot for all 60 images.png')

# # 3d image
# # fig = plt.figure(num=None, figsize=(4, 3), dpi=80, facecolor='w', edgecolor='k')
# fig = plt.figure()
# # figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
# # fig, axs = plt.subplots(nrows=1, ncols=1, constrained_layout=True)
# ax = Axes3D(fig)
# ax.scatter(Z[0:5, 0], Z[0:5, 1], Z[0:5, 2], s = 100,  marker = 'x', c = 'r', label = 'NaCl 10mM, CaCl2 3.0mM, MgCl2 1.5mM')
# ax.scatter(Z[5:10, 0], Z[5:10, 1], Z[5:10, 2], s = 100, marker = 's', c = 'r', label = 'NaCl 5.0mM, CaCl2 3.0mM, MgCl2 1.5mM')
# ax.scatter(Z[10:15, 0], Z[10:15, 1], Z[10:15, 2], s = 100, marker = 'o', c ='r', label =  'NaCl 2.5mM, CaCl2 3.0mM, MgCl2 1.5mM')
#
# ax.scatter(Z[15:20, 0], Z[15:20, 1], Z[15:20, 2], s = 100, marker = 'x', c = 'g', label = 'NaHCO3 10mM, CaCl2 0.5mM, MgCl2 0.25mM')
# ax.scatter(Z[20:25, 0], Z[20:25, 1], Z[20:25, 2], s = 100, marker = 's', c = 'g', label = 'NaHCO3 5.0mM, CaCl2 0.5mM, MgCl2 0.25mM')
# ax.scatter(Z[25:30, 0], Z[25:30, 1], Z[25:30, 2], s = 100, marker = 'o', c = 'g', label = 'NaHCO3 2.5mM, CaCl2 0.5mM, MgCl2 0.25mM')
#
# ax.scatter(Z[30:35, 0], Z[30:35, 1], Z[30:35, 2], s = 100, marker = 'x', c = 'b', label = 'Na2SO4 5.0mM, CaSO4 0.5mM, MgSO4 0.25mM')
# ax.scatter(Z[35:40, 0], Z[35:40, 1], Z[35:40, 2], s = 100, marker = 's', c = 'b', label = 'Na2SO4 2.5mM, CaSO4 0.5mM, MgSO4 0.25mM')
# ax.scatter(Z[40:45, 0], Z[40:45, 1], Z[40:45, 2], s = 100, marker = 'o', c = 'b', label='Na2SO4 1.25mM, CaSO4 0.5mM, MgSO4 0.25mM')
#
# ax.scatter(Z[45:50, 0], Z[45:50, 1], Z[45:50, 2], s = 100, marker = 'x', c = 'y', label = 'NaHCO3 10mM, CaSO4 0.5mM, MgSO4 0.25mM')
# ax.scatter(Z[50:55, 0], Z[50:55, 1], Z[50:55, 2], s = 100, marker = 's', c = 'y', label = 'NaHCO3 5.0mM, CaSO4 0.5mM, MgSO4 0.25mM')
# ax.scatter(Z[55:60, 0], Z[55:60, 1], Z[55:60, 2], s = 100, marker = 'o', c = 'y', label = 'NaHCO3 2.5mM, CaSO4 0.5mM, MgSO4 0.25mM')
#
# ax.set_xlabel('First component', fontsize = 15)
# ax.set_ylabel('Second component', fontsize = 15)
# ax.set_zlabel('Third component', fontsize = 15)
# ax.set_title('PCA image analysis for all samples \n with three components', fontsize = 20)
# ax.legend(loc = 'upper right', prop={'size': 7})
# plt.show()
# plt.close(fig)