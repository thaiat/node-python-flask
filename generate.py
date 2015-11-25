import numpy as np
from PIL import Image
from imutils import convenience
import cv2
from random import randint


# image = cv2.imread('./images/fifaref3.png')
# im = Image.open('./images/grey.jpg')
# im2 = Image.open('./images/fifaref2.jpg')
# im2 = im2.resize([200, 249])
# # im.paste(im2)
# im.save('./images/generated/greytest.jpg')
# im3 = Image.blend(im,im2,0.5)
# im3.save('./images/generated/aaaaa.jpg')

for i in range(0, 300):
    x_offset = randint(45, 55)
    y_offset = randint(57, 67)
    alpha = randint(0, 6) - 3

    pt1x = randint(0, 6) - 3
    pt2x = randint(0, 6) - 3
    pt3x = randint(0, 6) - 3
    pt1y = randint(0, 6) - 3
    pt2y = randint(0, 6) - 3
    pt3y = randint(0, 6) - 3

    rand_r = randint(0, 255)
    rand_g = randint(0, 255)
    rand_b = randint(0, 255)

    background = cv2.imread("./images/grey.jpg")

    for j in range(0, 374):
        for k in range(0, 300):
            background.itemset((j, k, 0), rand_r)
            background.itemset((j, k, 1), rand_g)
            background.itemset((j, k, 2), rand_b)

    foreground = cv2.imread("./images/fifa_resized.jpg")
    cv2.imwrite('./images/generated/ORIGIN.jpg', foreground)

    background[y_offset:y_offset+foreground.shape[0],
               x_offset:x_offset+foreground.shape[1]] = foreground

    rotated = convenience.rotate(background, alpha)

    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32(
        [[50+pt1x, 50+pt1y], [200+pt2x, 50+pt2y], [50+pt3x, 200+pt3y]])
    M = cv2.getAffineTransform(pts1, pts2)

    rows, cols, ch = background.shape
    affineTransformed = cv2.warpAffine(rotated, M, (cols, rows))

    final = affineTransformed[44:330, 35:265]  # cropping the image keeping the right proportions

    cv2.imwrite('./images/generated/' + str(i) + '.jpg', final)
