import numpy as np


def classification10k(data_temp, transfo_temperature, dim):
    """
    Classifies pixels into temperature groups and assigns them one color per class.

    Args:
    - data_temp: The data extracted from the csv.
    - transfo_temperature: The matrix of correspondences, temperature/color.
    - dim: The dimension wanted for the image

    Return:
    - res: The function returns an array of RGB values which represents the initial image transformed into pyrometric color grouped by 10K.
    """
    # Initialization
    res = np.zeros(dim)

    # Treatment
    for y in range(dim[0]):  # y
        for x in range(dim[1]):  # x
            if data_temp.iloc[1936 * y + x, 2] >= 1495:
                res[y][x] = transfo_temperature[-1][1]

            elif data_temp.iloc[1936 * y + x, 2] < 295:
                res[y][x] = [255, 255, 255]

            else:
                ecart = 3000
                temp = 0
                k = 0
                while k < len(transfo_temperature)-1:
                    a = abs(transfo_temperature[k][0] - data_temp.iloc[1936 * y + x, 2])
                    if a < ecart:
                        ecart = a
                        temp = k
                        k += 1
                    else:
                        k = len(transfo_temperature)-1

                res[y][x] = transfo_temperature[temp][1]
    return res


def mask10k(transfo_temperature, dim, classification):
    """
    Classifies pixels into temperature groups and assigns them one color per class.

    Args:
    - transfo_temperature: The matrix of correspondences, temperature/color.
    - dim: The dimension wanted for the image
    - classification: The array which contains the RGB image in pyrometric color classes

    Return:
    - masks: The array returned contains the matrix mask for each temperature
    """
    masks = []
    for k in range(len(transfo_temperature)):
        mask1 = np.zeros(dim)
        for y in range(dim[0]):  # y
            for x in range(dim[1]):
                classe = classification[y][x]
                trans = transfo_temperature[k][1]
                if classe[0] == trans[0] and classe[1] == trans[1] and classe[2] == trans[2]:
                    mask1[y][x] = trans
                else:
                    mask1[y][x] = [0, 0, 0]
        mask1 = mask1.astype(np.uint8)
        masks.append([transfo_temperature[k][0], mask1])
    return masks
