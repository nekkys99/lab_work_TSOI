from PIL import Image
import numpy as np
import sys
import cv2
from matplotlib import pyplot as plt


def median_filter(data, filter_size):
    temp = []
    indexer = filter_size // 2
    data_final = []
    data_final = np.zeros((len(data), len(data[0])))
    for i in range(len(data)):

        for j in range(len(data[0])):

            for z in range(filter_size):
                if i + z - indexer < 0 or i + z - indexer > len(data) - 1:
                    for c in range(filter_size):
                        temp.append(0)
                else:
                    if j + z - indexer < 0 or j + indexer > len(data[0]) - 1:
                        temp.append(0)
                    else:
                        for k in range(filter_size):
                            temp.append(data[i + z - indexer][j + k - indexer])

            temp.sort()
            data_final[i][j] = temp[len(temp) // 2]
            temp = []
    return data_final


def main(argv):

    img = cv2.imread('gray11.png', 0)
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    plt.hist(img.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.show()

    img = Image.open("gray11.png").convert("L")
    arr = np.array(img)
    removed_noise = median_filter(arr, 5)  ## Второй аргумент позволяет настроить сетку для изображения
    img = Image.fromarray(removed_noise)
    img.show()
    img.convert("RGB").save("median_fake1.png")

    img = cv2.imread('median_fake1.png', 0)
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    plt.hist(img.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.show()


if __name__ == "__main__":
    main(sys.argv)