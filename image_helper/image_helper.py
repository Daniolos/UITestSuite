import cv2
import numpy as np


def locate_icon_center_on_image(screenshot_path, icon_path, threshold=0.6):

    image = cv2.imread(screenshot_path)
    template = cv2.imread(icon_path)

    w, h = template.shape[1], template.shape[0]

    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)

    for pt in zip(*loc[::-1]):
        center_x = pt[0] + w // 2
        center_y = pt[1] + h // 2
        return (center_x, center_y)

    raise Exception("No icon could be located on screen.")
