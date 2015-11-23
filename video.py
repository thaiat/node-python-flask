import re
import cStringIO
import sys
from PIL import Image
import numpy as np
import cv2

IMAGE_SIZE = 200.0
IMAGE_PADDING = 10
MATCH_THRESHOLD = 400
orb = cv2.ORB(1000, 1.2)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
cascade = cv2.CascadeClassifier('classifier/fifa.xml')
reference = cv2.imread('images/fifaref.jpg')
reference = cv2.cvtColor(reference, cv2.COLOR_RGB2GRAY)
ratio = IMAGE_SIZE/reference.shape[1]
reference = cv2.resize(
    reference, (int(IMAGE_SIZE), int(reference.shape[0]*ratio)))
kp_r, des_r = orb.detectAndCompute(reference, None)


def process(content):
    if not isinstance(content, str):
        return []
    image_data = re.sub('^data:image/.+;base64,', '', content).decode('base64')
    image = Image.open(cStringIO.StringIO(image_data))
    image = cv2.cvtColor(np.array(image), 2)
    # cv2.imwrite('images/' + uuid + '.jpg', image)
    #image = cv2.imread('images/slack_for_ios_upload.png')
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    faces = cascade.detectMultiScale(image, 1.03, 20)
    if(len(faces) <= 0):
        return []

    good = []
    for (x, y, w, h) in faces:

        obj = gray[(y-IMAGE_PADDING):(y+h+IMAGE_PADDING),
                   (x-IMAGE_PADDING):(x+w+IMAGE_PADDING)]
        if obj.shape[0] == 0 or obj.shape[1] == 0:
            continue
        ratio = IMAGE_SIZE/obj.shape[1]
        obj = cv2.resize(obj, (int(IMAGE_SIZE), int(obj.shape[0]*ratio)))
        #cv2.imwrite('tmp/'+ 'processed' + str(i) +'.jpg', obj)
        # find the keypoints and descriptors for object
        kp_o, des_o = orb.detectAndCompute(obj, None)
        if len(kp_o) == 0:
            continue

        # match descriptors
        matches = bf.match(des_r, des_o)
        # matches = sorted(matches, key=lambda x: x.distance)
        # print(str(len(matches)))
        # store all the good matches as per Lowe's ratio test.
        # Draw first 10 matches.
        #img3 = python_utils.drawMatches(reference, kp_r, obj, kp_o, good[:10])
        #cv2.imwrite('tmp/'+ 'processed-matches' + str(i) +'.jpg', img3)

        # draw object on street image, if threshold met
        #print('image ' + str(i) + ' ' + str(len(good)))
        # print(len(matches))
        if(len(matches) >= MATCH_THRESHOLD):
            good.append({'x': x, 'y': y, 'width': w, 'height': h})

    return good
