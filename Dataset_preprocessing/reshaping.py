import os
import cv2 as cv
import numpy as np
from PIL import Image
from tqdm import tqdm

"""
Reshaping of all the actual and pyrometric for  both of the fluctual and steady datasets. 
Necessary for the right processing of the UNet

"""


fluctual = r"C:\Users\marie\PycharmProjects\UNet2\Images_fluctual"
steady = r"C:\Users\marie\PycharmProjects\UNet2\Images_steady"

for i in tqdm(range(1, 101)):
    nom_steady_actual = 'frame' + str(i) + '.png'
    nom_steady_actual = os.path.join(steady, "Actual", nom_steady_actual)
    image_steady_actual = cv.imread(nom_steady_actual)
    image_steady_actual = cv.cvtColor(image_steady_actual, cv.COLOR_BGR2RGB)
    image_steady_actual = image_steady_actual[168:1519, 130:2280]
    image_steady_actual = image_steady_actual.astype(np.uint8)
    image_steady_actual = Image.fromarray(image_steady_actual)
    image_steady_actual = image_steady_actual.resize((1936, 1216), Image.LANCZOS)
    image_steady_actual.save(nom_steady_actual, optimize=True, quality=95)

    nom_steady_pyro = 'frame' + str(i) + '.png'
    nom_steady_pyro = os.path.join(steady, "Pyro", nom_steady_pyro)
    image_steady_pyrometric = cv.imread(nom_steady_pyro)
    image_steady_pyrometric = cv.cvtColor(image_steady_pyrometric, cv.COLOR_BGR2RGB)
    image_steady_pyrometric = image_steady_pyrometric[168:1519, 130:2280]
    image_steady_pyrometric = image_steady_pyrometric.astype(np.uint8)
    image_steady_pyrometric = Image.fromarray(image_steady_pyrometric)
    image_steady_pyrometric = image_steady_pyrometric.resize((1936, 1216), Image.LANCZOS)
    image_steady_pyrometric.save(nom_steady_pyro, optimize=True, quality=95)

    nom_fluctual_actual = 'frame' + str(i) + '.png'
    nom_fluctual_actual = os.path.join(fluctual, "Actual", nom_fluctual_actual)
    image_fluctual_actual = cv.imread(nom_fluctual_actual)
    image_fluctual_actual = cv.cvtColor(image_fluctual_actual, cv.COLOR_BGR2RGB)
    image_fluctual_actual = image_fluctual_actual[93:1593, 13:2402]
    image_fluctual_actual = image_fluctual_actual.astype(np.uint8)
    image_fluctual_actual = Image.fromarray(image_fluctual_actual)
    image_fluctual_actual = image_fluctual_actual.resize((1936, 1216), Image.LANCZOS)
    image_fluctual_actual.save(nom_fluctual_actual, optimize=True, quality=95)

    nom_fluctual_pyro = 'frame' + str(i) + '.png'
    nom_fluctual_pyro = os.path.join(fluctual, "Pyro", nom_fluctual_pyro)
    image_fluctual_pyrometric = cv.imread(nom_fluctual_pyro)
    image_fluctual_pyrometric = cv.cvtColor(image_fluctual_pyrometric, cv.COLOR_BGR2RGB)
    image_fluctual_pyrometric = image_fluctual_pyrometric[93:1593, 13:2402]
    image_fluctual_pyrometric = image_fluctual_pyrometric.astype(np.uint8)
    image_fluctual_pyrometric = Image.fromarray(image_fluctual_pyrometric)
    image_fluctual_pyrometric = image_fluctual_pyrometric.resize((1936, 1216), Image.LANCZOS)
    image_fluctual_pyrometric.save(nom_fluctual_pyro, optimize=True, quality=95)
