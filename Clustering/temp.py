import cv2 as cv

# Creation of the scale temperature/pixel with a pyrometric picture
# Opening of the pyrometric picture
image = cv.imread('steady_scaled_image.png')
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)


# Matches between temperature and the value of the RGB pixel
pix_y = 699  # pixels counter
t = 300  # temperatures counter
transfo_temperature = []  # matrix doing the link between temperature and RGB pixel values


for j in range(3):
    # 58
    # 6*8
    for i in range(8):
        pix_R = image[pix_y][1055][0]
        pix_G = image[pix_y][1055][1]
        pix_B = image[pix_y][1055][2]
        transfo_temperature.append([t, [pix_R, pix_G, pix_B]])
        t += 10
        pix_y -= 6

    # 5*2
    for i in range(2):
        pix_R = image[pix_y][1055][0]
        pix_G = image[pix_y][1055][1]
        pix_B = image[pix_y][1055][2]
        transfo_temperature.append([t, [pix_R, pix_G, pix_B]])
        t += 10
        pix_y -= 5

    # 56
    # 6*6
    for i in range(6):
        pix_R = image[pix_y][1055][0]
        pix_G = image[pix_y][1055][1]
        pix_B = image[pix_y][1055][2]
        transfo_temperature.append([t, [pix_R, pix_G, pix_B]])
        t += 10
        pix_y -= 6

    # 6*4
    for i in range(4):
        pix_R = image[pix_y][1055][0]
        pix_G = image[pix_y][1055][1]
        pix_B = image[pix_y][1055][2]
        transfo_temperature.append([t, [pix_R, pix_G, pix_B]])
        t += 10
        pix_y -= 5


# 56
# 6*6
for i in range(6):
    pix_R = image[pix_y][1055][0]
    pix_G = image[pix_y][1055][1]
    pix_B = image[pix_y][1055][2]
    transfo_temperature.append([t, [pix_R, pix_G, pix_B]])
    t += 10
    pix_y -= 6

# 5*4
for i in range(4):
    pix_R = image[pix_y][1055][0]
    pix_G = image[pix_y][1055][1]
    pix_B = image[pix_y][1055][2]
    transfo_temperature.append([t, [pix_R, pix_G, pix_B]])
    t += 10
    pix_y -= 5


for j in range(2):
    # 56
    # 6*6
    for i in range(6):
        pix_R = image[pix_y][1055][0]
        pix_G = image[pix_y][1055][1]
        pix_B = image[pix_y][1055][2]
        transfo_temperature.append([t, [pix_R, pix_G, pix_B]])
        t += 10
        pix_y -= 6

    # 5*4
    for i in range(4):
        pix_R = image[pix_y][1055][0]
        pix_G = image[pix_y][1055][1]
        pix_B = image[pix_y][1055][2]
        transfo_temperature.append([t, [pix_R, pix_G, pix_B]])
        t += 10
        pix_y -= 5

    # 58
    # 6*8
    for i in range(8):
        pix_R = image[pix_y][1055][0]
        pix_G = image[pix_y][1055][1]
        pix_B = image[pix_y][1055][2]
        transfo_temperature.append([t, [pix_R, pix_G, pix_B]])
        t += 10
        pix_y -= 6

    # 5*2
    for i in range(2):
        pix_R = image[pix_y][1055][0]
        pix_G = image[pix_y][1055][1]
        pix_B = image[pix_y][1055][2]
        transfo_temperature.append([t, [pix_R, pix_G, pix_B]])
        t += 10
        pix_y -= 5


# 56
# 6*6
for i in range(6):
    pix_R = image[pix_y][1055][0]
    pix_G = image[pix_y][1055][1]
    pix_B = image[pix_y][1055][2]
    transfo_temperature.append([t, [pix_R, pix_G, pix_B]])
    t += 10
    pix_y -= 6

# 6*4
for i in range(4):
    pix_R = image[pix_y][1055][0]
    pix_G = image[pix_y][1055][1]
    pix_B = image[pix_y][1055][2]
    transfo_temperature.append([t, [pix_R, pix_G, pix_B]])
    t += 10
    pix_y -= 5

while pix_y > 19:
    pix_R = image[pix_y][1055][0]
    pix_G = image[pix_y][1055][1]
    pix_B = image[pix_y][1055][2]
    transfo_temperature.append([t, [pix_R, pix_G, pix_B]])
    t += 10
    pix_y -= 6

pix_R = transfo_temperature[-1][1][0]
pix_G = transfo_temperature[-1][1][1] - 3
pix_B = transfo_temperature[-1][1][2]
transfo_temperature.append([t, [pix_R, pix_G, pix_B]])