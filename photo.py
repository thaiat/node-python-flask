from imutils import convenience
import cv2
import utils


def variance_of_laplacian(image):
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    return cv2.Laplacian(image, cv2.CV_64F).var()


def blur_analysis(content, threshold):
    if not isinstance(content, unicode):
        return []

    result = []

    if content[:4] == 'http':
        image = convenience.url_to_image(content, readFlag=cv2.IMREAD_COLOR)
        # image = cv2.imread('./images/image-test/10.jpg')
    else:
        image = utils.b64_to_image(content)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = variance_of_laplacian(gray)
    text = "Not Blurry"

    if fm < threshold:
        text = "Blurry"

    result.append({'text': text, 'focus': fm*1})

    return result
