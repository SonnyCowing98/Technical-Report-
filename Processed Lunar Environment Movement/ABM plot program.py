import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import colorConverter
import matplotlib as mpl

crop = np.load('crop1.npy')
crop1 = crop

path = np.load('pathLE.npy')





# create dummy data
zvals = crop
zvals2 = path

# generate the colors for your colormap
color1 = colorConverter.to_rgba('white')
color2 = colorConverter.to_rgba('red')

# make the colormaps
cmap1 = mpl.colors.LinearSegmentedColormap.from_list('my_cmap',['white','black'],256)
cmap2 = mpl.colors.LinearSegmentedColormap.from_list('my_cmap2',[color1,color2],256)

cmap2._init() # create the _lut array, with rgba values

# create your alpha array and fill the colormap with them.
# here it is progressive, but you can create whathever you want
alphas = np.linspace(0, 0.8, cmap2.N+3)
cmap2._lut[:,-1] = alphas

img2 = plt.imshow(zvals, interpolation='nearest', cmap=cmap1, origin='lower')
img3 = plt.imshow(zvals2, interpolation='nearest', cmap=cmap2, origin='lower')

plt.show()