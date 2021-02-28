# Assignment-1
### image processing codes

#import statement blocks

import numpy as np 
import matplotlib.pyplot as plt 

brain_image=plt.imread("Brain.jpg") 
plt.imshow(brain_image)
plt.title('Display Image read using imread()') 
plt.axis('off')

#show the image
plt.show()

#show the dimensions
brain_image.shape
plt.show()

import numpy as np 
import matplotlib.pyplot as plt 

brain_image=plt.imread("Brain.jpg") 
plt.imshow(brain_image)
plt.title('Display Image read using imread()') 
plt.axis('off')
plt.show()

plt.show()

#plotting the histogram
plt.hist(brain_image, bins=10)
plt.show()

from scipy import ndimage

#using different gaussian kernels for smoothing

filter1 = ndimage.gaussian_filter(brain_image, sigma=5)

plt.imshow(filter1)
plt.imshow(filter1, cmap='Greys_r')
plt.show()
plt.hist(filter1, bins=10)
plt.show()

filter2 = ndimage.gaussian_filter(brain_image, sigma=10)

plt.imshow(filter2)
plt.imshow(filter2, cmap='Greys_r')
plt.show()
plt.hist(filter2, bins=10)
plt.show()

filter3 = ndimage.gaussian_filter(brain_image, sigma=20)

plt.imshow(filter3)
plt.imshow(filter3, cmap='Greys_r')
plt.show()
plt.hist(filter3, bins=10)
plt.show()

filter4 = ndimage.gaussian_filter(brain_image, sigma=30)

plt.imshow(filter4)
plt.imshow(filter4, cmap='Greys_r')
plt.show()
plt.hist(filter4, bins=10)
plt.show()

filter5 = ndimage.gaussian_filter(brain_image, sigma=40)

plt.imshow(filter5)
plt.imshow(filter5, cmap='Greys_r')
plt.show()
plt.hist(filter5, bins=10)
plt.show()

filter6 = ndimage.gaussian_filter(brain_image, sigma=50)

plt.imshow(filter6)
plt.imshow(filter6, cmap='Greys_r')
plt.show()
plt.hist(filter6, bins=10)
plt.show()
