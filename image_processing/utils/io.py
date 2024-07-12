from skimage.io import imsave, imread


def read_image(path, is_gray=False):
    image = imread(path, as_grey=is_gray)
    return image


def save_image(image, path):
    imsave(path, image)
