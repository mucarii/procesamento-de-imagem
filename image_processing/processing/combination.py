import numpy as np
from skimage import io
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity
import matplotlib.pyplot as plt


def find_difference(image1, image2):
    assert image1.shape == image2.shape, "especifique 2 imagens do mesmo tamanho"
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)
    (score, diff) = structural_similarity(gray_image1, gray_image2, full=True)
    print("similaridade: ", score)
    normalized_difference_image = (diff - diff.min()) / (diff.max() - diff.min())
    return normalized_difference_image


def transfer_histogram(image1, image2):
    matched_image = match_histograms(image1, image2, multichannel=True)
    return matched_image


# Carregar imagens de exemplo
image1 = io.imread("caminho_para_imagem1.jpg")
image2 = io.imread("caminho_para_imagem2.jpg")

# Encontrar diferença
difference_image = find_difference(image1, image2)

# Transferir histograma
matched_image = transfer_histogram(image1, image2)

# Mostrar resultados
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
ax1.imshow(image1)
ax1.set_title("Imagem 1")
ax1.axis("off")

ax2.imshow(image2)
ax2.set_title("Imagem 2")
ax2.axis("off")

ax3.imshow(difference_image, cmap="gray")
ax3.set_title("Diferença Normalizada")
ax3.axis("off")

plt.show()

# Mostrar imagem com histograma transferido
plt.figure()
plt.imshow(matched_image)
plt.title("Imagem com Histograma Transferido")
plt.axis("off")
plt.show()
