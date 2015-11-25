import re
import cStringIO
from PIL import Image
import numpy as np
import cv2
from imutils.object_detection import non_max_suppression

IMAGE_SIZE = 200.0
IMAGE_PADDING = 10
MATCH_THRESHOLD = 400
orb = cv2.ORB(1000, 1.2)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
#cascade = cv2.CascadeClassifier('classifier/fifa.xml')
#reference = cv2.imread('images/fifaref2.jpg')
cascade = cv2.CascadeClassifier('classifier/swbattlefront.xml')
reference = cv2.imread('images/swbattlefront.jpg')

reference = cv2.cvtColor(reference, cv2.COLOR_RGB2GRAY)
ratio = IMAGE_SIZE/reference.shape[1]
reference = cv2.resize(
    reference, (int(IMAGE_SIZE), int(reference.shape[0]*ratio)))
kp_r, des_r = orb.detectAndCompute(reference, None)


def process(content):
    if not isinstance(content, unicode):
        return []
    image_data = re.sub('^data:image/.+;base64,', '', content).decode('base64')
    image = Image.open(cStringIO.StringIO(image_data))
    image = cv2.cvtColor(np.array(image), 2)
    # cv2.imwrite('image.jpg', image)

    # gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    faces = cascade.detectMultiScale(image, 1.03, 500, minSize=(10, 10))

    if(len(faces) <= 0):
        return []

    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in faces])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.15)

    good = []
    for (x, y, x2, y2) in pick:
        good.append(
            {'x': x*1, 'y': y*1, 'width': (x2-x)*1, 'height': (y2-y)*1})

    # for f in good:
    #    cv2.rectangle(
    #        image,
    #        (f.get('x'), f.get('y')),
    #        (f.get('width'), f.get('height')),
    #        (0, 255, 0), 6)
    #    cv2.imwrite('image.jpg', image)

    return good
