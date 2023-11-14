import numpy as np
from tqdm import tqdm


def shape_change(image):
    cropped = image[209:1398, 150:2043]  # remove the axes
    # cropped = image[670:940, 540:1820]   # maximum reducing
    return cropped


def blue_removal(matrice):
    size = matrice.shape
    for i in range(size[0]):
        for j in range(size[1]):
            matrice[i][j][2] = 0
    return matrice


def transfer_matrix_creation(natural, treated):
    size = natural.shape
    # transfer = matrix used to transpose natural/pyrometric
    transfer = [[natural[0][0], treated[0][0]]]  # initialization for while
    for i in range(size[0]):
        for j in range(size[1]):
            k = 0
            c = 0  # counter for the number of iterations in the while loop
            while k < len(transfer):
                c += 1
                b0 = natural[i][j][0]
                b1 = natural[i][j][1]
                # for RGB treatment
                # if b0 == transfer[k][0][0] and b1 == transfer[k][0][1] and natural[i][j][2] == transfer[k][0][2]:
                # for blue removal RG treatment
                if b0 == transfer[k][0][0] and b1 == transfer[k][0][1]:
                    k = len(transfer)
                else:
                    k += 1
            if c == k:
                transfer.append([natural[i][j], treated[i][j]])
    return transfer


def treatment1_tot(original, trans):
    size = original.shape
    res = np.zeros((size[0], size[1], size[2]))
    for i in range(size[0]):
        for j in range(size[1]):
            res[i][j] = treatment1_pix(original[i][j], trans)
    return res


def treatment1_pix(pixel, trans):
    for i in range(len(trans)):
        # for RGB treatment
        # if pixel[0] == trans[i][0][0] and pixel[1] == trans[i][0][1] and pixel[2] == trans[i][0][2]:
        # for blue removal so RG treatment
        if pixel[0] == trans[i][0][0] and pixel[1] == trans[i][0][1]:
            return trans[i][1]
    return [0, 0, 0]


def temperature_matrix(temp,  mat):
    size = mat.shape
    mat_temp = np.zeros((size[0], size[1], size[2]))
    for i in range(size[0]):
        for j in range(size[1]):
            mat_temp[i][j] = temperature_pixel(temp, mat[i][j])
    return mat_temp


def temperature_pixel(temp, pix):
    gap = []
    for i in range(len(temp)):
        gap.append(abs(temp[i][1][0] - pix[0])+abs(temp[i][1][1] - pix[1])+abs(temp[i][1][2] - pix[2]))
    return np.argmin(gap)


def differences(treated, pyro):
    d = 0
    size = treated.shape
    for i in range(size[0]):
        for j in range(size[1]):
            t = treated[i][j][0]
            if t != pyro[i][j][0] or treated[i][j][1] != pyro[i][j][1] or treated[i][j][2] != pyro[i][j][2]:
                d += 1
    return d


def differences_tol(tol, treated, pyr):
    d = 0
    size = treated.shape
    for i in range(size[0]):
        for j in range(size[1]):
            a = abs(treated[i][j][0]-pyr[i][j][0])
            b = abs(treated[i][j][1]-pyr[i][j][1])
            c = abs(treated[i][j][2]-pyr[i][j][2])
            if a + b + c > tol:
                d += 1
    return d


def temperature_difference(treated, wanted):
    right = 0
    less_5 = 0
    from5to10 = 0
    from10to15 = 0
    from15to20 = 0
    more_20 = 0
    size = treated.shape
    for i in range(size[0]):
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
