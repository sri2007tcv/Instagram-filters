import cv2
import matplotlib.pyplot as plt
import numpy as np
image=cv2.imread('fantastic-beasts-.png')
row, column = image.shape[:2]
kernel_x=cv2.getGaussianKernel(column,200)
kernel_y=cv2.getGaussianKernel(row,200)
kernel=kernel_y*kernel_x.T
filter=255*kernel/np.linalg.norm(kernel)
vintage_img=np.copy(image)
for i in range(3):
   vintage_img[:,:,i]=vintage_img[:,:,i]*filter
plt.imshow(vintage_img)
plt.show()
