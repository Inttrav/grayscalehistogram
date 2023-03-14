import cv2
import matplotlib.pyplot as p


img = cv2.imread('image.jpg')


img = cv2.resize(img, (1920,1080))
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
p.xlabel("Shade of gray")
p.ylabel("NO. of times found in image")
p.hist(img.flatten(),256,[0,255])
p.title("Histogram")
p.show()

