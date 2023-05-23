#imports
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from main import number_of_pendulums
class Plotting():
    def __init__(self, pendulum_number, pendulum_list, dataframe, y):
        self.pendulum_number = pendulum_number
        self.pendulum_list = pendulum_list
        self.dataframe = dataframe
        self.y = y
    # here a list is created where each item is the full data for one pendulum
    def create_pendulum_data_list(self):
        for k in range(1, self.pendulum_number+1):
            p = self.dataframe.loc[self.dataframe['pendulum'] == k]
            self.pendulum_list.append(p)

    # this loop plots the correct data inside each list item of thependulum list
    def create_plotting_data(self):
        for i in range(0, self.pendulum_number):
            damping = list((self.pendulum_list[i])['damping'])[0]
            plt.plot(list((self.pendulum_list[0])['time']), list((self.pendulum_list[i])[self.y]), label=damping)

    def create_plotting_data_for_energies(self):
        for i in range(0, self.pendulum_number):
            plt.plot(list((self.pendulum_list[0])['time']), list((self.pendulum_list[i])[self.y]), label=self.y)