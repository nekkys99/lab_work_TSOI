import numpy as np
import cv2
import matplotlib.pyplot as plt
import sys


def main(argv):
    ##Вставьте изображения для сравнения
    image = cv2.imread('gray5.png', cv2.IMREAD_GRAYSCALE)
    image_1 = cv2.resize(image, (int(image.shape[1] / 1.6), int(image.shape[0] / 1.6)))
    image_3 = cv2.imread('median_fake5.png', cv2.IMREAD_GRAYSCALE)

    image_weight = int(image_1.shape[0] / 2)
    resized_image_weight = int(image_3.shape[0] / 2)

    hist_image = []
    hist_image_3 = []

    for i in range(0, image_1.shape[1]):
        hist_image.append(image_1[image_weight][i])

    for i in range(0, image_3.shape[1]):
        hist_image_3.append(image_3[resized_image_weight][i])

    plt.subplot(221)
    x = np.arange(0, image_1.shape[1], 1)
    plt.plot(x, hist_image)

    plt.subplot(222)
    x = np.arange(0, image_3.shape[1], 1)
    plt.plot(x, hist_image_3)

    plt.show()


if __name__ == "__main__":
    main(sys.argv)
