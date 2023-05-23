#imports
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from main import number_of_pendulums
from plotting_methods import Plotting
# the data frame is opended and read here
dframe = pd.read_excel('dataframe.xlsx')

#create the figure
fig = plt.figure()
ax = fig.gca()

list_of_pendulum_data =[]

plots_list= []

def generate_list_of_plots():
    plotting1 = Plotting(pendulum_number =number_of_pendulums, pendulum_list = list_of_pendulum_data, dataframe = dframe, y = 'Kinetic energy')
    plotting2 = Plotting(pendulum_number =number_of_pendulums, pendulum_list = list_of_pendulum_data, dataframe = dframe, y = 'Potential energy')
    plotting3 = Plotting(pendulum_number =number_of_pendulums, pendulum_list = list_of_pendulum_data, dataframe = dframe, y = 'Total energy')
    plots_list.append(plotting1)
    plots_list.append(plotting2)
    plots_list.append(plotting3)

generate_list_of_plots()

for p in plots_list:
    p.create_pendulum_data_list()
    p.create_plotting_data_for_energies()


# here the plot is customized
plt.xlabel('Time (seconds)')
plt.ylabel('Energy (J)')
ax.tick_params(axis='x', direction='in') # x ticks point in 
ax.tick_params(axis='y', direction='in') # y ticks point in
ax.set_title('')
plt.legend(title='')
plt.show()