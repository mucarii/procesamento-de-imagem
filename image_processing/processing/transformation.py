from skimage.transform import resize


def resize_image(image, proportion):
    assert 0 <= proportion <= 1, "especifique uma proporção entre 0 e 1"
    height = int(image.shape[0] * proportion)
    width = int(image.shape[1] * proportion)
    image_resized = resize(image, (height, width), anti_aliasing=True)
    return image_resized
