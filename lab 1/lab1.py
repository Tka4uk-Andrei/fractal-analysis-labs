import numpy as np
import scipy
import cv2


def boxCounting(Z, size):
        S = np.add.reduceat(
                np.add.reduceat(Z, np.arange(0, Z.shape[0], size), axis=0),
                np.arange(0, Z.shape[1], size), axis=1)

        count = 0
        for x in range(S.shape[0]):
            for y in range(S.shape[1]):
                if S[x][y] > 0 & S[x][y] < size * size:
                    count += 1
        return count


def fractalDimension(Z, threshold=0.6):
    Z = (Z < threshold)
    a = min(Z.shape)
    n1 = 2**np.floor(np.log(a)/np.log(2))
    n2 = int(np.log(n1)/np.log(2))
    sizes = 2**np.arange(n2, 1, -1)
    counts = []
    for size in sizes:
        counts.append(boxCounting(Z, size))

    leastSquares = np.polyfit(np.log(sizes), np.log(counts), 1)  
    return -leastSquares[0]


def printRes(img_name):
    original = cv2.imread(img_name)

    h, w, c= original.shape
    print (img_name + " height = ", h)
    print (img_name + " widh   = ", w)

    grayIm = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    threshold=cv2.threshold(grayIm, 127, 255, cv2.THRESH_BINARY)[0] / 255
    print(img_name + " Фрактальная размерность: ", fractalDimension(grayIm, threshold))


printRes('img1.jpg')
printRes('img2.jpg')
printRes('img3.jpg')
printRes('img4.jpg')
