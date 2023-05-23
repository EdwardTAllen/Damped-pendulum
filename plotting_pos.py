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
x = [0]*500
list_of_pendulum_data =[]
time = list(dframe['time'])
plotting1 = Plotting(pendulum_number =number_of_pendulums, pendulum_list = list_of_pendulum_data, dataframe = dframe, y = 'pos')

plotting1.create_pendulum_data_list()
plotting1.create_plotting_data()
#plt.plot(time, x, linestyle='dashed')


# here the plot is customized
plt.xlabel('Time (seconds)')
plt.ylabel('angular position (radians)')
ax.tick_params(axis='x', direction='in') # x ticks point in 
ax.tick_params(axis='y', direction='in') # y ticks point in
ax.set_title('')
plt.legend(title='Damping coefficients')
plt.show()