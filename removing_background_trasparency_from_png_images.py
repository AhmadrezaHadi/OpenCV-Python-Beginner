import numpy as np
import cv2


# this function removes transparency and converts it to a grayscale
def remove_transparency(source, background_color):
    source_img = cv2.cvtColor(source[:, :, :3], cv2.COLOR_BGR2GRAY)
    source_mask = source[:, :, 3] * (1 / 255.0)

    background_mask = 1.0 - source_mask

    bg_part = (background_color * (1 / 255.0)) * background_mask
    source_part = (source_img * (1 / 255.0)) * source_mask

    return np.uint8(cv2.addWeighted(bg_part, 255.0, source_part, 255.0, 0.0))


def png_background_fix(src):
    # make mask of where the transparent bits are
    trans_mask = src[:, :, 3] == 0

    # replace areas of transparency with white and not transparent
    src[trans_mask] = [255, 255, 255, 255]

    # new image without alpha channel...
    return cv2.cvtColor(src, cv2.COLOR_BGRA2BGR)
