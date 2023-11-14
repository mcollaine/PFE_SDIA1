from sklearn.cluster import KMeans
from tqdm import tqdm
import numpy as np


def shape_change(image):
    cropped = image[168:1352, 130:2151]
    # cropped = image[209:1398, 150:2043]  # remove the axes
    # cropped = image[540:1820, 670:940]   # maximum reducing
    return cropped


def blue_removal(matrix):
    """
    To process only on RG values, the blue pixel is removed.

    Arg:
    - matrix (array): Matrix representing the actual image

    Return:
    - matrix (array): Matrix representing the actual image without the blue value
    """
    size = matrix.shape
    for i in range(size[0]):
        for j in range(size[1]):
            matrix[i][j][2] = 0
    return matrix


def flattening_mat(matrix):
    res = []
    size = matrix.shape
    for i in range(size[0]):
        for j in range(size[1]):
            res.append([matrix[i][j][0], matrix[i][j][1]])
    return res


def transfer_matrix_creation(actual, treated):
    size = actual.shape
    transfer = [[actual[0][0], treated[0][0]]]
    for i in tqdm(range(size[0])):
        for j in range(size[1]):
            k = 0
            c = 0
            while k < len(transfer):
                c += 1
                b0 = actual[i][j][0]
                b1 = actual[i][j][1]
                if b0 == transfer[k][0][0] and b1 == transfer[k][0][1] and actual[i][j][2] == transfer[k][0][2]:
                    k = len(transfer)
                else:
                    k += 1
            if c == k:
                transfer.append([actual[i][j], treated[i][j]])
    return transfer


def clustering(n, img):
    kmeans = KMeans(n_clusters=n, n_init=10)
    kmeans.fit(img)
    labels = kmeans.labels_
    centroid = kmeans.cluster_centers_
    labels1 = list(labels)  # on associe à chaque pixel son cluster
    return centroid, labels1


def normalization(centroid):
    (n, m) = centroid.shape
    for i in range(n):
        for j in range(m):
            centroid[i][j] = round(centroid[i][j])
    return centroid


def label_values_allocation(centroid, labels):
    res = []
    for i in tqdm(range(len(labels))):
        f = labels[i]
        res.append(centroid[f-1])
    return labels


def treatment_tot(trans, liste):
    color_pyro = []
    for i in tqdm(range(len(liste))):
        color_pyro.append(treatment_pix(liste[i], trans))
    return color_pyro


def treatment_pix(pixel, trans):
    for i in range(len(trans)):
        # for RGB treatment
        if pixel[0] == trans[i][0][0] and pixel[1] == trans[i][0][1] and pixel[2] == trans[i][0][2]:
            # for blue removal so RG treatment
            # if pixel[0] == trans[i][0][0] and pixel[1] == trans[i][0][1]:
            return trans[i][1]
    return [0, 0, 0]


def differences_tol(tol, traite, pyr):
    d = 0
    taille = traite.shape
    for i in tqdm(range(taille[0])):
        for j in range(taille[1]):
            a = abs(traite[i][j][0]-pyr[i][j][0])
            b = abs(traite[i][j][1]-pyr[i][j][1])
            c = abs(traite[i][j][2]-pyr[i][j][2])
            if a + b + c > tol:
                d += 1
    return d


def differences(traite, pyro):
    d = 0
    e = 0
    taille = traite.shape
    for i in tqdm(range(taille[0])):
        for j in range(taille[1]):
            t = traite[i][j][0]
            if t != pyro[i][j][0] or traite[i][j][1] != pyro[i][j][1] or traite[i][j][2] != pyro[i][j][2]:
                d += 1
            if traite[i][j].any() == 255:
                e += 1
    return d, e


def matrix_volume_setting(size, liste):
    res = np.zeros(size)
    for i in range(size[0]):
        for j in range(size[1]):
            res[i][j] = liste[i+j]
    return res


def temperature_centroid(temp,  cent):
    for i in tqdm(range(len(cent))):
        cent[i] = pixel_temperature(temp, cent[i])
    return cent


def pixel_temperature(temp, pix):
    ecart = []
    for i in range(len(temp)):
        ecart.append(abs(temp[i][1][0] - pix[0])+abs(temp[i][1][1] - pix[1])+abs(temp[i][1][2] - pix[2]))
    return np.argmin(ecart)


def matrix_temperature(temp,  mat):
    taille = mat.shape
    mat_temp = np.zeros((taille[0], taille[1], taille[2]))
    for i in tqdm(range(taille[0])):
        for j in range(taille[1]):
            mat_temp[i][j] = pixel_temperature(temp, mat[i][j])
    return mat_temp


def difference_temperature(treated, wanted):
    right = 0
    less_5 = 0
    from5to10 = 0
    from10to15 = 0
    from15to20 = 0
    more_20 = 0
    size = treated.shape
    for i in tqdm(range(size[0])):
        for j in range(size[1]):
            a = abs(treated[i][j][0] - wanted[i][j][0]) + abs(treated[i][j][1] - wanted[i][j][1])
            b = abs(treated[i][j][2] - wanted[i][j][2])
            if a + b >= 20:
                more_20 += 1
            if 15 <= a + b < 20:
                from15to20 += 1
            if 10 <= a + b < 15:
                from10to15 += 1
            if 5 <= a + b < 10:
                from5to10 += 1
            if 0 < a + b < 5:
                less_5 += 1
            if a + b == 0:
                right += 1
    return right, less_5, from5to10, from10to15, from15to20, more_20
