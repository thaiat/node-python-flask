import numpy as np
import sys

from imutils import convenience
import cv2

# import any special Python 2.7 packages
if sys.version_info.major == 2:
    from urllib import urlopen

# import any special Python 3 packages
elif sys.version_info.major == 3:
    from urllib.request import urlopen


def variance_of_laplacian(image):
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    return cv2.Laplacian(image, cv2.CV_64F).var()


def blur_analysis(url, threshold):
    result = []
    image = convenience.url_to_image(url, readFlag=cv2.IMREAD_COLOR)
    # image = cv2.imread('./images/image-test/10.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = variance_of_laplacian(gray)
    text = "Not Blurry"

    if fm < threshold:
        text = "Blurry"

    result.append({'text': text, 'focus': fm*1})

    return result
