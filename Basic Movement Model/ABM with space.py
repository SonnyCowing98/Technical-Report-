from MoneyModel_AddingSpace import ModelClass
import numpy as np
import matplotlib.pyplot as plt 
from PIL import Image 





g = ModelClass(5, 20, 50)
for i in range(5):
    g.step()






# Not very sure on what is happening here at first glace 
agent_counts = np.zeros((g.grid.width, g.grid.height))
for cell in g.grid.coord_iter():
    cell_content, x, y = cell
    agent_count = len(cell_content)
    agent_counts[x][y] = agent_count
plt.imshow(agent_counts, interpolation='nearest')
plt.colorbar()
plt.show()
