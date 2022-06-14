import cv2
import matplotlib.pyplot as plt
image=cv2.imread('fantastic-beasts-.png')
bst=cv2.GaussianBlur(image, (5,5), cv2.BORDER_DEFAULT)
plt.imshow(bst)
plt.show()

