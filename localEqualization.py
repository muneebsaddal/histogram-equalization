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
    img = cv2.imread("test.png",0)
    showHist(img)

    #Local Histogram equalization using tiling approach
    newImage_0 = np.zeros((img.shape))
    height, width = img.shape[:2]
    for i in range(0, width/2):
        for j in range(0, height/2):
            newImage_0[i:width/2, j:height/2] = equalHist(img[i:width/2, j:height/2])   
    for i in range(width/2, width):
        for j in range(0, height/2):
            newImage_0[i:width, j:height/2] = equalHist(img[i:width, j:height/2])
    for i in range(0, width/2):
        for j in range(height/2, height):
            newImage_0[i:width/2, j:height] = equalHist(img[i:width/2, j:height])
    for i in range(width/2, width):
        for j in range(height/2, height):
            newImage_0[i:width, j:height] = equalHist(img[i:width, j:height])
    cv2.imwrite("equalized_tiling.png", newImage_0)
    showHist(newImage_0)

    #Local Histogram equalization using tiling approach
    newImage_1 = np.zeros((img.shape))
    windowSize = 64
    for i in range(0,img.shape[0]-windowSize):
        for j in range(0,img.shape[1]-windowSize):
            newImage_1[i: i + windowSize, j: j + windowSize] = equalHist(img[i: i + windowSize, j: j + windowSize])
    cv2.imwrite("equalized_sliding.png", newImage_1)
    showHist(newImage_1)
