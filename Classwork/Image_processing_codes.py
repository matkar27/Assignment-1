# Assignment-1
### image processing codes

import numpy as np 
import matplotlib.pyplot as plt 

brain_image=plt.imread("Brain.jpg") 
plt.imshow(brain_image)
plt.title('Display Image read using imread()') 
plt.axis('off')
plt.show()

brain_image.shape
plt.show()

import numpy as np 
import matplotlib.pyplot as plt 

brain_image=plt.imread("Brain.jpg") 
plt.imshow(brain_image)
plt.title('Display Image read using imread()') 
plt.axis('off')
plt.show()
plt.imshow(brain_image, cmap='Greys_r')
plt.show()

plt.hist(brain_image, bins=10)
plt.show()
