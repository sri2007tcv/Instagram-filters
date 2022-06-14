import cv2
import matplotlib.pyplot as plt
image=cv2.imread('fantastic-beasts-.png')
edge=cv2.Canny(image,100,300)
plt.imshow(edge)
plt.show()