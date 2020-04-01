from mesa import Agent, Model 
from mesa.time import RandomActivation
from mesa.space import MultiGrid
import numpy as np


apath = []
class AgentClass(Agent): 
    """An agent with fixed initial wealth."""
    
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    # The move function facilitates the movement of the agents around the grid    
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
        self.pos,
        moore=True, 
        include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
    
    # The agentpath function add the positions of the agents to the apath list 
    def agentpath(self):
        apath.append(self.pos)
    
    # The step function calls the move and agentpath function each time it is called
    def step(self):
        self.move()
        self.agentpath()
        


class ModelClass(Model):
    """A model with some number of agents."""
    def __init__(self, N, width, height):
        self.num_agents = N
        # MultiGrid function used to create the 2D model environment 
        self.grid = MultiGrid(width, height, False)
        # RandomActivation reshuffles the schedule each time the function is called 
        self.schedule = RandomActivation(self)
        
        # This loop created the agents and adds them to the schedule 
        for i in range(self.num_agents):
            a = AgentClass(i, self)
            self.schedule.add(a)
            # Add the agents to a random cell 
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x,y))


    def step(self):
        '''Advance the model by one step.'''
        self.schedule.step()

