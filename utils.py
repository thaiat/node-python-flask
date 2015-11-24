import re
from PIL import Image
import numpy as np
import cv2
import cStringIO


def b64_to_image(content):
    image_data = re.sub('^data:image/.+;base64,', '', content).decode('base64')
    image = Image.open(cStringIO.StringIO(image_data))
    image = cv2.cvtColor(np.array(image), 2)
    # cv2.imwrite('image.jpg', image)
    return image
