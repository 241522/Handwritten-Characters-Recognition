import numpy
import numpy as np
from PIL import Image

THRESHOLD_FOR_BLACK = 180


def rescale_image(im, size=28, fill_color=255):
    x, y = im.size
    ratio = max(x, y) / 28

    im = im.resize((int(x / ratio), int(y / ratio)))
    x, y = im.size
    new_im = Image.new('L', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im


def get_pixels(im):
    return numpy.asarray(im)


def get_negative(pixels):
    return 255 - pixels


def thresholding(im):
    for i in range(0, im.size[0] - 1):
        for j in range(0, im.size[1] - 1):
            pixel = im.getpixel((i, j))
            if pixel> THRESHOLD_FOR_BLACK:
                pixel = 255
            else:
                pixel = 0
            im.putpixel((i, j), pixel)
    return im


def normalize(pixels):
    return pixels / 255


def reshape(pixels):
    return np.reshape(pixels, (1, 28, 28, 1))


def process_image(im):
    im = im.convert("L")
    im = thresholding(im)
    im = rescale_image(im)
    pixels = get_pixels(im)
    pixels = reshape(
        normalize(
            get_negative(
                pixels)))
    return pixels


def read_mapping(filepath):
    mapping = dict()
    with open(filepath) as f:
        for line in f:
            split_line = line.split(" ")
            mapping[int(split_line[0])] = int(split_line[1])
    return mapping
