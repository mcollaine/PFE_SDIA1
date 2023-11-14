import numpy as np
import matplotlib.pyplot as plt
import cv2
from sklearn.cluster import KMeans
import operator as op


# image pyro

I1 = cv2.imread('frame1_pyro.png')
I2 = cv2.cvtColor(I1, cv2.COLOR_BGR2RGB)
img = I2.reshape((-1, 3))

# image flame

img2 = cv2.imread('frame1_750.png')
Im2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img2 = Im2.reshape((-1, 3))

# nombre de clusters

n = 20

# clustering avec KMeans pyro

kmeans = KMeans(n_clusters=n, n_init=10)
s = kmeans.fit(img)
labels = kmeans.labels_
centroid = kmeans.cluster_centers_
labels1 = list(labels)   # on associe à chaque pixel son cluster

# clustering avec KMeans flamme

kmeans2 = KMeans(n_clusters=n, n_init=10)
s2 = kmeans2.fit(img2)
labels2 = kmeans2.labels_
centroid2 = kmeans2.cluster_centers_
labels2 = list(labels2)   # on associe à chaque pixel son cluster

# Centroid fixe
percent1 = []
percent2 = []
for i in range(n):
    percent1.append(op.countOf(labels1, i)*100/len(labels1))
    percent2.append(op.countOf(labels2, i)*100/len(labels2))

same = []
y = []

for i in range(n):
    x = []
    Min = 0
    indice = 0
    for j in range(n):
        x.append(abs(percent1[i]-percent2[j]))
    Min = min(x)
    y.append(Min)
    for k in range(n):
        if x[k] == Min:
            same.append(k)

# créateur d'images
X = []
X2 = []


for i in range(0, n):
    image = np.zeros_like(img)
    # image2=imageblanche(img2)
    image2 = np.zeros_like(img2)
    for j in range(image.shape[0]):
        if labels1[j] == i:
            image[j] = centroid[i]
    X.append(image)
    for k in range(image2.shape[0]):
        if labels2[k] == i:
            image2[k] = centroid2[i]
    X2.append(image2)


for i in range(n):
    plt.subplot(2, n, i+1)
    plt.imshow(X[i].reshape(np.shape(I1)))
    plt.title(i)
    plt.axis('off')
    plt.subplot(2, n, n+i+1)
    plt.imshow(X2[i].reshape(np.shape(Im2)))
    plt.title(i)
    plt.axis('off')
    
# reconstitution d'image pyro

RecoPyro = np.zeros_like(img)
for i in range(0, n):
    RecoPyro = RecoPyro+X[i]
    
# reconstitution d'image normale

RecoFla = np.zeros_like(img2)
for i in range(0, n):
    RecoFla = RecoFla+X2[i]
    
plt.figure()
plt.subplot(1, 4, 1)
plt.imshow(RecoPyro.reshape(np.shape(I1)))
plt.subplot(1, 4, 2)
plt.imshow(I2)
plt.subplot(1, 4, 3)
plt.imshow(RecoFla.reshape(np.shape(Im2)))
plt.subplot(1, 4, 4)
plt.imshow(Im2)

# transformation

L = np.zeros_like(img2)

for i in range(len(labels2)):
    for j in range(n):
        if labels2[i] == j:
            L[i] = centroid[same[j]]

        
plt.figure()
plt.subplot(1, 3, 1)
plt.imshow(L.reshape(np.shape(Im2)))
plt.title('reconstitution')
plt.subplot(1, 3, 2)
plt.imshow(RecoPyro.reshape(np.shape(I1)))
plt.title('clusters')
plt.subplot(1, 3, 3)
plt.imshow(I2)
plt.title('real one')
        
        