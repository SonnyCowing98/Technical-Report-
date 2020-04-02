import numpy as np 
import matplotlib.pyplot as plt 
from PIL import Image 

# Sample.jpg assigned to data variable 
data = Image.open('sample.jpg')

# Converts data to greyscale (0-255) and converts data to a numpy array 
data = data.convert('L')
data = np.array(data)

# Retrieves gradients in x and y dimensions and stores results in numpy arrays 
xy,xx= np.gradient(data)
xy = np.array(xy)
xx = np.array(xx)

# This is where the range of acceptable gradients is defined (for each dimension)
resultxy = np.where(np.logical_and(xy>-50, xy<50))
resultxx = np.where(np.logical_and(xx>-50, xx<50))

# Numpy zeros array must be the same shape as the input data 
plotarrayxy = np.zeros(np.array(data).shape)
plotarrayxx = np.zeros(np.array(data).shape)

# Indexing the np.zeros arrays to equal 1 where the conditions are met
plotarrayxy[resultxy] = 1
plotarrayxx[resultxx] = 1

# Stating the conditions needed to compare plotarrayxy and plotarrayxx 
c1 = (plotarrayxy == 1)
c2 = (plotarrayxx == 1)

# Retrieving the location where both conditions c1 and c2 are met 
result1 = np.where(c1 & c2)

# Creating an array that displays a 1 where the gradients are within the specified range
plotarray = np.zeros(np.array(data).shape)
plotarray[result1] = 1

# Converting data type to uint8
finalplot = plotarray.astype(np.uint8)

# Create the plot 
plt.imshow(data, cmap = 'Greys')
plt.imshow(finalplot, cmap = 'Greys')


# Display the plot 
plt.show()
