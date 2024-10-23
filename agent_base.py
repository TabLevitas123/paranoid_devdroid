
import random
import logging
import numpy as np
from sklearn.neural_network import MLPClassifier

class Agent:
    def __init__(self, name, task):
        self.name = name
        self.task = task
        self.sub_agents = []
        self.is_active = True
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.DEBUG)

    def create_sub_agent(self, sub_agent_name, sub_agent_task):
        try:
            sub_agent = Agent(sub_agent_name, sub_agent_task)
            self.sub_agents.append(sub_agent)
            self.logger.info(f"Sub-agent {sub_agent_name} created successfully.")
            return sub_agent
        except Exception as e:
            self.logger.error(f"Failed to create sub-agent {sub_agent_name}: {str(e)}")
            return None

    def communicate(self, message):
        try:
            print(f"Agent {self.name} says: {message}")
            self.logger.info(f"Message communicated: {message}")
        except Exception as e:
            self.logger.error(f"Error in communication: {str(e)}")
    
    def coordinate_agents(self):
        for agent in self.sub_agents:
            if agent.is_active:
                agent.communicate(f"Task update from {self.name}: {self.task}")
    
    def deactivate(self):
        self.is_active = False
        self.logger.info(f"Agent {self.name} deactivated.")
    
    def activate(self):
        self.is_active = True
        self.logger.info(f"Agent {self.name} activated.")
