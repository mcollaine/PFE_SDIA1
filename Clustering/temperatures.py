import cv2 as cv

# Creation of the scale temperature/pixel with a pyrometric picture
# Opening of the pyrometric picture
image = cv.imread('frame1_pyro.png')
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

# Matches between temperature and the value of the RGB pixel
pix_y = 1587  # pixels counter
t = 400  # temperatures counter
temperature = []  # matrix doing the link between temperature and RGB pixel values
c = 0  # counter of scales between two graduation in the image
d = 0  # counter for the alternation 76/74 pixels

# Initialization from 400 to 440K
for s in range(5):
    pix_R = 0
    pix_G = 0
    pix_B = 0
    # Many pixels for one temperature so average of pixels values
    for i in range(2062, 2076):
        pix_R = pix_R + image[pix_y][i][0]
        pix_G = pix_G + image[pix_y][i][1]
        pix_B = pix_B + image[pix_y][i][2]
    # Rouding to stay in RGB format
    pix_R = round(pix_R / 15)
    pix_G = round(pix_G / 15)
    pix_B = round(pix_B / 15)
    temperature.append([t, [pix_R, pix_G, pix_B]])
    c += 1
    if c == 5:
        pix_y -= 1
        c = 0
    t += 10
    pix_y -= 15

while pix_y > 18:
    pix_R = 0
    pix_G = 0
    pix_B = 0
    # Many pixels for one temperature so average of pixels values
    for i in range(2062, 2077):
        pix_R = pix_R + image[pix_y][i][0]
        pix_G = pix_G + image[pix_y][i][1]
        pix_B = pix_B + image[pix_y][i][2]
    # Rouding to stay in RGB format
    pix_R = round(pix_R / 15)
    pix_G = round(pix_G / 15)
    pix_B = round(pix_B / 15)
    temperature.append([t, [pix_R, pix_G, pix_B]])
    c += 1
    if c == 5:
        if d == 0:
            pix_y -= 1
            d = 1
        else:
            pix_y += 1
            d = 0
        c = 0
    t += 10
    pix_y -= 15

pix_R = temperature[-1][1][0]
pix_G = temperature[-1][1][1] - 6
pix_B = temperature[-1][1][2] + 1

temperature.append([t, [pix_R, pix_G, pix_B]])
