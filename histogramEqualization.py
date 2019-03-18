import cv2
import numpy as np
import matplotlib.pyplot as plt

def showHist(img):
    plt.hist(img.ravel(), bins=256, range=(0.0, 255.0))
    plt.show()

def equalHist(img):
    data = img.copy().flatten()
    hist, bins = np.histogram(data, 256, density=True)
    cdf = hist.cumsum()
    cdf = 255 * cdf / cdf[-1]
    equalImg = np.interp(data, bins[:-1], cdf)
    return equalImg.reshape(img.shape)

if __name__ == "__main__":
    img = cv2.imread('img.tif', 0)
    showHist(img)
    equalImg = equalHist(img)
    showHist(equalImg)
    cv2.imwrite("equalized.png", equalImg)
