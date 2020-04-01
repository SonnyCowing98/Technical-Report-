from mesa import Agent, Model 
from mesa.time import RandomActivation
from mesa.space import MultiGrid
import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib as mpl
from matplotlib.colors import colorConverter


crop = np.zeros((100,100), dtype = np.uint8)
crop[:] = np.arange(100)
crop1 = crop

# Specifying the number of agents and the number of steps they take
num_of_agents = 5
N = num_of_agents
num_of_steps = 49



# Variable is ready to collect the data from self.pos
apath = []
xx = []
yy = []



class MoneyAgent(Agent): 
    """An agent with fixed initial wealth."""
    
    # def is how you create a function. A function in a class describes the objects behaivour of the class
    #__init__ sets the initial values of an object. It does not need to be called to be initialised
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
   
    
    def decider(self, ModelEnvironment, position):
       
        i , j = position

        
        # retrieves the cell neighbors 
        region = ModelEnvironment[max(0,i-1) : i+2,max(0,j-1) : j+2] 
        
        current = region[1,1]
        # region[1,1] = 0      


        
        
        
        # This line decides if the agents want to move to larger values or smaller values 
        PossipleSteps = np.where(region > current )
        row, column = PossipleSteps
        row_len =  row.shape
        rand = row_len[0] 
       


        x = random.sample(range(rand),1)

    

        
    
        np.array(x)
        x = x[0]
        yy = column[x]
        xx =    row[x]
        
       
        while yy == 1 and xx == 1:
            x = random.sample(range(rand),1)
            x = x[0]
            yy = column[x]
            xx =    row[x]

            if yy != 1 or xx !=1:
                break 

        

        if xx == 0 and yy == 0:
            return 2
        elif xx == 0 and yy == 1:
            return 4
        elif xx == 0 and yy == 2:
            return 7
        elif xx== 1 and yy== 0:
            return 1
        elif xx == 1 and yy == 2:
            return 6
        elif xx == 2 and yy == 0:
            return 0
        elif xx == 2 and yy == 1:
            return 3
        elif xx == 2 and yy == 2:
            return 5
    
          


    # The following function allows the agent to choose its new position on the grid
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
        self.pos,
        moore=True, 
        include_center=False)
        
        # This is where the number of the cell will be inputted
        new_position = possible_steps[self.decider(crop,self.pos)]
        # new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    
    # This function saves the path of the agents to the apath variable
    def agentpath(self):
        apath.append(self.pos)    
        
    
    def step(self):
        self.move()
        self.agentpath()
        
        

# The object in this class is the MoneyModel
class MoneyModel(Model):
    """A model with some number of agents."""
    
    def __init__(self, N, elevation):
        # num_agents is a parameter and stays constant throughout the simulation
        self.num_agents = N
        self.width = elevation.shape[0]
        self.height = elevation.shape[1]
        self.z = elevation   
        # Adds the grid to the model object 
        self.grid = MultiGrid(self.width, self.height, True)
        # Adds the scheduler to the model object 
        self.schedule = RandomActivation(self)
        
        # create agents (for loop hence multiple agents) and add them to the schedular (one at a time) 
        for i in range(self.num_agents):
            # The money agent class (object) is being computed for every value of i
            a = MoneyAgent(i, self)
            self.schedule.add(a)
            self.grid.place_agent(a, (50,50))


    def step(self):
        '''Advance the model by one step.'''
        self.schedule.step()

# Calls the class and the init function 
model1 = MoneyModel(num_of_agents , crop)

# Runs the model for as many times as stated in num_of_steps
for i in range(num_of_steps):
    model1.step()

Apath = np.array(apath)

# print(Apath.shape)
agent1y = Apath[:,0]
agent1x = Apath[:,1]
agent1pathplot = agent1y ,agent1x
pathplot = np.zeros((100,100), dtype = np.uint8)
pathplot[agent1pathplot] = 1

# create dummy data
zvals = crop1
zvals2 = pathplot

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

