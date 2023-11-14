import cv2 as cv

# Creation of the scale temperature/pixel with a pyrometric picture
# Opening of the pyrometric picture
image = cv.imread('Scaled_image.png')
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)


# Matches between temperature and the value of the RGB pixel
pix_y = 699  # pixels counter
t = 300  # temperatures counter
transfo_temperature_10K = []  # matrix doing the link between temperature and RGB pixel values


for j in range(3):
    # 58
    # 6*8
    for i in range(8):
        pix_R = image[pix_y][1055][0]
        pix_G = image[pix_y][1055][1]
        pix_B = image[pix_y][1055][2]
        transfo_temperature_10K.append([t, [pix_R, pix_G, pix_B]])
        t += 10
        pix_y -= 6

    # 5*2
    for i in range(2):
        pix_R = image[pix_y][1055][0]
        pix_G = image[pix_y][1055][1]
        pix_B = image[pix_y][1055][2]
        transfo_temperature_10K.append([t, [pix_R, pix_G, pix_B]])
        t += 10
        pix_y -= 5

    # 56
    # 6*6
    for i in range(6):
        pix_R = image[pix_y][1055][0]
        pix_G = image[pix_y][1055][1]
        pix_B = image[pix_y][1055][2]
        transfo_temperature_10K.append([t, [pix_R, pix_G, pix_B]])
        t += 10
        pix_y -= 6

    # 6*4
    for i in range(4):
        pix_R = image[pix_y][1055][0]
        pix_G = image[pix_y][1055][1]
        pix_B = image[pix_y][1055][2]
        transfo_temperature_10K.append([t, [pix_R, pix_G, pix_B]])
        t += 10
        pix_y -= 5


# 56
# 6*6
for i in range(6):
    pix_R = image[pix_y][1055][0]
    pix_G = image[pix_y][1055][1]
    pix_B = image[pix_y][1055][2]
    transfo_temperature_10K.append([t, [pix_R, pix_G, pix_B]])
    t += 10
    pix_y -= 6

# 5*4
for i in range(4):
    pix_R = image[pix_y][1055][0]
    pix_G = image[pix_y][1055][1]
    pix_B = image[pix_y][1055][2]
    transfo_temperature_10K.append([t, [pix_R, pix_G, pix_B]])
    t += 10
    pix_y -= 5


for j in range(2):
    # 56
    # 6*6
    for i in range(6):
        pix_R = image[pix_y][1055][0]
        pix_G = image[pix_y][1055][1]
        pix_B = image[pix_y][1055][2]
        transfo_temperature_10K.append([t, [pix_R, pix_G, pix_B]])
        t += 10
        pix_y -= 6

    # 5*4
    for i in range(4):
        pix_R = image[pix_y][1055][0]
        pix_G = image[pix_y][1055][1]
        pix_B = image[pix_y][1055][2]
        transfo_temperature_10K.append([t, [pix_R, pix_G, pix_B]])
        t += 10
        pix_y -= 5

    # 58
    # 6*8
    for i in range(8):
        pix_R = image[pix_y][1055][0]
        pix_G = image[pix_y][1055][1]
        pix_B = image[pix_y][1055][2]
        transfo_temperature_10K.append([t, [pix_R, pix_G, pix_B]])
        t += 10
        pix_y -= 6

    # 5*2
    for i in range(2):
        pix_R = image[pix_y][1055][0]
        pix_G = image[pix_y][1055][1]
        pix_B = image[pix_y][1055][2]
        transfo_temperature_10K.append([t, [pix_R, pix_G, pix_B]])
        t += 10
        pix_y -= 5


# 56
# 6*6
for i in range(6):
    pix_R = image[pix_y][1055][0]
    pix_G = image[pix_y][1055][1]
    pix_B = image[pix_y][1055][2]
    transfo_temperature_10K.append([t, [pix_R, pix_G, pix_B]])
    t += 10
    pix_y -= 6

# 6*4
for i in range(4):
    pix_R = image[pix_y][1055][0]
    pix_G = image[pix_y][1055][1]
    pix_B = image[pix_y][1055][2]
    transfo_temperature_10K.append([t, [pix_R, pix_G, pix_B]])
    t += 10
    pix_y -= 5

while pix_y > 19:
    pix_R = image[pix_y][1055][0]
    pix_G = image[pix_y][1055][1]
    pix_B = image[pix_y][1055][2]
    transfo_temperature_10K.append([t, [pix_R, pix_G, pix_B]])
    t += 10
    pix_y -= 6

pix_R = transfo_temperature_10K[-1][1][0]
pix_G = transfo_temperature_10K[-1][1][1] - 3
pix_B = transfo_temperature_10K[-1][1][2]
transfo_temperature_10K.append([t, [pix_R, pix_G, pix_B]])
transfo_temperature_10K.append([0, [255, 255, 255]])


transfo_temperature_50K = []
transfo_temperature_100K = []

for k in range(len(transfo_temperature_10K)):
    if (transfo_temperature_10K[k][0] % 50) == 0:
        transfo_temperature_50K.append(transfo_temperature_10K[k])
    if (transfo_temperature_10K[k][0] % 100) == 0:
        transfo_temperature_100K.append(transfo_temperature_10K[k])


# Saving of the results
with open('trans_temp_10K', "w") as fichier:
    for k in range(len(transfo_temperature_10K)):
        ligne_str = str(transfo_temperature_10K[k][0]) + ',' + str(transfo_temperature_10K[k][1])
        fichier.write(ligne_str + "\n")

with open('trans_temp_50K', "w") as fichier:
    for k in range(len(transfo_temperature_50K)):
        ligne_str = str(transfo_temperature_50K[k][0]) + ',' + str(transfo_temperature_50K[k][1])
        fichier.write(ligne_str + "\n")

with open('trans_temp_100K', "w") as fichier:
    for k in range(len(transfo_temperature_100K)):
        ligne_str = str(transfo_temperature_100K[k][0]) + ',' + str(transfo_temperature_100K[k][1])
        fichier.write(ligne_str + "\n")
