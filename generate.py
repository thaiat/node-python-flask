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

for i in range(0, 30):
    x_offset = randint(20, 30)
    y_offset = randint(25, 35)
    alpha = randint(0, 6) - 3

    pt1x = randint(0, 6) - 3
    pt2x = randint(0, 6) - 3
    pt3x = randint(0, 6) - 3
    pt1y = randint(0, 6) - 3
    pt2y = randint(0, 6) - 3
    pt3y = randint(0, 6) - 3

    background = cv2.imread("./images/grey.jpg")
    foreground = cv2.imread("./images/fifa_resized.jpg")
    cv2.imwrite('./images/generated/ORIGIN.jpg', foreground)

    rows, cols, ch = background.shape

    # shifted = imutils.translate(image, -100 + 10*i, -100 + 10*i)
    background[y_offset:y_offset+foreground.shape[0],
               x_offset:x_offset+foreground.shape[1]] = foreground

    rotated = convenience.rotate(background, alpha)

    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[50+pt1x, 50+pt1y], [200+pt2x, 50+pt2y], [50+pt3x, 200+pt3y]])
    M = cv2.getAffineTransform(pts1, pts2)

    affineTransformed = cv2.warpAffine(rotated, M, (cols, rows))

    cv2.imwrite('./images/generated/' + str(i) + '.jpg', affineTransformed)
