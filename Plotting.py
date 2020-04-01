import numpy as np 
import matplotlib.pyplot as plt 
from PIL import Image 
#from scipy import ndimage 

# sample.jpg assigned to data variable 
data = Image.open('sample.jpg')

# converts data to greyscale (0-255) and converts data to a numpy array 
data = data.convert('L')
data = np.array(data)

# retrieves gradients in x and y dimensions and stores results in numpy arrays 
xy,xx= np.gradient(data)
xy = np.array(xy)
xx = np.array(xx)

# This is where the range of acceptable gradients is defined (for each dimension)
resultxy = np.where(np.logical_and(xy>-50, xy<50))
resultxx = np.where(np.logical_and(xx>-50, xx<50))

# numpy zeros array must be the same shape as the input data 
plotarrayxy = np.zeros(np.array(data).shape)
plotarrayxx = np.zeros(np.array(data).shape)
print(np.array(data).shape)
# indexing the np.zeros arrays to equal 1 where the conditions are met
plotarrayxy[resultxy] = 1
plotarrayxx[resultxx] = 1

# stating the conditions needed to compare plotarrayxy and plotarrayxx 
c1 = (plotarrayxy == 1)
c2 = (plotarrayxx == 1)

# retrieving the location where both condtions c1 and c2 are met 
result1 = np.where(c1 & c2)

# creating an array that displays a 1 where the gradients are within the specified range
plotarray = np.zeros(np.array(data).shape)
plotarray[result1] = 1

# converting data type to uint8
finalplot = plotarray.astype(np.uint8)

# create the plot 
# plt.imshow(data, cmap = 'Greys')
# plt.imshow(finalplot, cmap = 'Greys')


## display the plot 
# plt.show()


##############################
# Saving a portion of the final plot for ABM

# crop1 = finalplot[95:165,365:460]
np.save('output.npy', finalplot)
# plt.imshow(crop1, cmap = 'Greys')
# plt.show()