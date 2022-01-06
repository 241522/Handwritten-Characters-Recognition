import numpy
import numpy as np
from PIL import Image


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


def thresholding(pixels):
    for i in range(0, 28):
        for j in range(0, 28):
            if pixels[i][j] > 180:
                pixels[i][j] = 255
            else:
                pixels[i][j] = 0
    return pixels


def normalize(pixels):
    return pixels / 255


def reshape(pixels):
    return np.reshape(pixels, (1, 28, 28, 1))


def process_image(im):
    im = rescale_image(im)
    pixels = get_pixels(im)
    pixels = reshape(
        normalize(
            get_negative(
                thresholding(pixels))))
    return pixels


def read_mapping():
    mapping = dict()
    with open("emnist-balanced-mapping.txt") as f:
        for line in f:
            split_line = line.split(" ")
            mapping[int(split_line[0])] = int(split_line[1])
    return mapping
