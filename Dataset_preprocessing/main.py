import os
import pandas as pd
from temperature_scale import *
from processing_10K import *
from processing_50K import *
from processing_100K import *
from tqdm import tqdm
from PIL import Image

# Settings
dimension = (1216, 1936, 3)
unet = r"C:\Users\marie\PycharmProjects\Dataset_preprocessing"


# # Steady
# for i in tqdm(range(1, 101)):
#     # Opening of the csv file
#     if i < 10:
#         nom = 'Pyrometry_data000' + str(i) + '.csv'
#     elif i == 100:
#         nom = 'Pyrometry_data0100.csv'
#     elif 10 <= i < 100:
#         nom = 'Pyrometry_data00' + str(i) + '.csv'
#     nom = os.path.join(unet, "Csv_steady", nom)
#
#     # Transformation of the csv file into the right format
#     with open(nom, 'r') as fichier:
#         contenu = fichier.read()
#
#     contenu = contenu.replace(';', ',')
#
#     with open(nom, 'w') as file:
#         file.write(contenu)
#
#     data_temp = pd.read_csv(nom)
#
#     # Pixels classification in groups of 10, 50 and 100K
#     classification_10K_std = classification10k(data_temp, transfo_temperature_10K, dimension)
#     classification_50K_std = classification50k(data_temp, transfo_temperature_50K, dimension)
#     classification_100K_std = classification100k(data_temp, transfo_temperature_100K, dimension)
#
#     # Creating and saving the ground truths
#     files_frame = "Frame" + str(i)
#     classification_10K_std = classification_10K_std.astype(np.uint8)
#     image10K_std = Image.fromarray(classification_10K_std)
#     nom10Kim_std = 'Groundtruth.png'
#     nom10Kim_std = os.path.join(unet, "Steady", "10K", files_frame, nom10Kim_std)
#     image10K_std.save(nom10Kim_std)
#
#     classification_50K_std = classification_50K_std.astype(np.uint8)
#     image50K_std = Image.fromarray(classification_50K_std)
#     nom50Kim_std = 'Groundtruth.png'
#     nom50Kim_std = os.path.join(unet, "Steady", "50K", files_frame, nom50Kim_std)
#     image50K_std.save(nom50Kim_std)
#
#     classification_100K_std = classification_100K_std.astype(np.uint8)
#     image100K_std = Image.fromarray(classification_100K_std)
#     nom100Kim_std = 'Groundtruth.png'
#     nom100Kim_std = os.path.join(unet, "Steady", "100K", files_frame, nom100Kim_std)
#     image100K_std.save(nom100Kim_std)
#
#     # Creating all masks
#     masks_10K_std = mask10k(transfo_temperature_10K, dimension, classification_10K_std)
#     masks_50K_std = mask50k(transfo_temperature_50K, dimension, classification_50K_std)
#     masks_100K_std = mask100k(transfo_temperature_100K, dimension, classification_100K_std)
#
#     nom10K = '10K_mask_1400.png'
#     nom50K = '50K_mask_1400.png'
#     nom100K = '100K_mask_1400.png'
#
#     # Printing all masks
#     # 10K masks
#     for k in range(len(transfo_temperature_10K)):
#         t = transfo_temperature_10K[k][0]
#         if t == 1400:
#             for p in range(len(masks_10K_std)):
#                 if t == masks_10K_std[p][0]:
#                     nom = 'Mask_' + str(t) + '.png'
#                     nom = os.path.join(unet, "Steady", "10K", files_frame, nom)
#                     image_mask10k = Image.fromarray(masks_10K_std[p][1])
#                     image_mask10k.save(nom10K)
#
#     # 50K masks
#     for k in range(len(transfo_temperature_50K)):
#         t = transfo_temperature_50K[k][0]
#         if t == 1400:
#             for p in range(len(masks_50K_std)):
#                 if t == masks_50K_std[p][0]:
#                     nom = 'Mask_' + str(t) + '.png'
#                     nom = os.path.join(unet, "Steady", "50K", files_frame, nom)
#                     image_mask50k = Image.fromarray(masks_50K_std[p][1])
#                     image_mask50k.save(nom50K)
#
#     # 100K masks
#     for k in range(len(transfo_temperature_100K)):
#         t = transfo_temperature_100K[k][0]
#         if t == 1400:
#             for p in range(len(masks_100K_std)):
#                 if t == masks_100K_std[p][0]:
#                     nom = 'Mask_' + str(t) + '.png'
#                     nom = os.path.join(unet, "Steady", "100K", files_frame, nom)
#                     image_mask100k = Image.fromarray(masks_100K_std[p][1])
#                     image_mask100k.save(nom100K)


# Fluctual
for i in tqdm(range(1, 101)):
    # Opening of the csv file
    if i < 10:
        nom = 'Pyrometry_data000' + str(i) + '.csv'
    elif i == 100:
        nom = 'Pyrometry_data0100.csv'
    elif 10 <= i < 100:
        nom = 'Pyrometry_data00' + str(i) + '.csv'
    nom = os.path.join(unet, "Csv_fluctual", nom)

    # Transformation of the csv file into the right format
    with open(nom, 'r') as fichier:
        contenu = fichier.read()

    contenu = contenu.replace(';', ',')

    with open(nom, 'w') as file:
        file.write(contenu)

    data_temp = pd.read_csv(nom)

    # Pixels classification in groups of 10, 50 and 100K
    classification_10K_ftl = classification10k(data_temp, transfo_temperature_10K, dimension)
    classification_50K_ftl = classification50k(data_temp, transfo_temperature_50K, dimension)
    classification_100K_ftl = classification100k(data_temp, transfo_temperature_100K, dimension)

    # Creating and saving the ground truths
    files_frame = "Frame" + str(i)
    classification_10K_ftl = classification_10K_ftl.astype(np.uint8)
    image10K_ftl = Image.fromarray(classification_10K_ftl)
    nom10Kim_ftl = 'Groundtruth.png'
    nom10Kim_ftl = os.path.join(unet, "Fluctual", "10K", files_frame, nom10Kim_ftl)
    image10K_ftl.save(nom10Kim_ftl)

    classification_50K_ftl = classification_50K_ftl.astype(np.uint8)
    image50K_ftl = Image.fromarray(classification_50K_ftl)
    nom50Kim_ftl = 'Groundtruth.png'
    nom50Kim_ftl = os.path.join(unet, "Fluctual", "50K", files_frame, nom50Kim_ftl)
    image50K_ftl.save(nom50Kim_ftl)

    classification_100K_ftl = classification_100K_ftl.astype(np.uint8)
    image100K_ftl = Image.fromarray(classification_100K_ftl)
    nom100Kim_ftl = 'Groundtruth.png'
    nom100Kim_ftl = os.path.join(unet, "Fluctual", "100K", files_frame, nom100Kim_ftl)
    image100K_ftl.save(nom100Kim_ftl)

    # Creating all masks
    masks_10K_ftl = mask10k(transfo_temperature_10K, dimension, classification_10K_ftl)
    masks_50K_ftl = mask50k(transfo_temperature_50K, dimension, classification_50K_ftl)
    masks_100K_ftl = mask100k(transfo_temperature_100K, dimension, classification_100K_ftl)

    # Printing all masks
    # 10K masks
    for k in range(len(transfo_temperature_10K)):
        t = transfo_temperature_10K[k][0]
        for p in range(len(masks_10K_ftl)):
            if t == masks_10K_ftl[p][0]:
                nom = 'Mask_' + str(t) + '.png'
                nom = os.path.join(unet, "Fluctual", "10K", files_frame, nom)
                image_mask10k = Image.fromarray(masks_10K_ftl[p][1])
                image_mask10k.save(nom)

    # 50K masks
    for k in range(len(transfo_temperature_50K)):
        t = transfo_temperature_50K[k][0]
        for p in range(len(masks_50K_ftl)):
            if t == masks_50K_ftl[p][0]:
                nom = 'Mask_' + str(t) + '.png'
                nom = os.path.join(unet, "Fluctual", "50K", files_frame, nom)
                image_mask50k = Image.fromarray(masks_50K_ftl[p][1])
                image_mask50k.save(nom)

    # 100K masks
    for k in range(len(transfo_temperature_100K)):
        t = transfo_temperature_100K[k][0]
        for p in range(len(masks_100K_ftl)):
            if t == masks_100K_ftl[p][0]:
                nom = 'Mask_' + str(t) + '.png'
                nom = os.path.join(unet, "Fluctual", "100K", files_frame, nom)
                image_mask100k = Image.fromarray(masks_100K_ftl[p][1])
                image_mask100k.save(nom)
