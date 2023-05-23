#imports
from pendulum import Pendulum
import numpy as np
import pandas as pd 

#time frame conditions
time_length = 30
num_steps = 500
step_size = time_length/num_steps
time_lables = list(range(1,num_steps +1)) # list of integers same numer of steps
times = np.linspace(0, time_length, num=num_steps)
# pendulum changable variables
mass = 1
length = 1
y_0 = np.array([np.radians(10.0), 0.0]) # pos and angular velocity

#list of data (get rid of replace with data frame)
anglular_position_list = []
angular_velocity_list = []
time_list = []
data = []
data_euler = []
data_ralston = []
data_rk4 = []
pendulum_list = []

def create_pendulum_list():
    '''
    Here is a function where different pendulum objects
    can be created and appended to the 'pendulum_list'
    '''
    # creating pendulum objects
    pendulum2 = Pendulum(length=length, mass=mass,damping=0.4, y_0=y_0)
    pendulum3 = Pendulum(length=length, mass=mass,damping=3.5, y_0=y_0)
    pendulum4 = Pendulum(length=length, mass=mass,damping=5.8, y_0=y_0) # c = 5.6, need .5 .6. .8
    pendulum5 = Pendulum(length=length, mass=mass,damping=6.0, y_0=y_0) # 24
    #appedning pendulum objects to a list
    pendulum_list.append(pendulum2)
    pendulum_list.append(pendulum3)
    pendulum_list.append(pendulum4)
    pendulum_list.append(pendulum5)

create_pendulum_list()
number_of_pendulums = len(pendulum_list)

#main loop
pendulum_number = 0
for p in pendulum_list:
    yn = y_0
    pendulum_number = pendulum_number+1
    for t in times:
        yn = p.RK4_method(dt=step_size, yn=yn)  #add this for RK4
        #yn = ralston_method(dt=step_size, yn=yn, pendulum = p) # add this for raslton
        #yn = forward_euler_method(dt=step_size, yn=yn, pendulum = p) # add this for forward euler
        Ek = p.kinetic_energy(yn=yn)
        Ep = p.potential_energy(yn=yn)
        Et = Ek+Ep
        angular_position = yn[0]
        angular_velocity = yn[1]
        data.append(np.array([angular_position, angular_velocity, t, pendulum_number, p.damping, Ek, Ep, Et], dtype = float))
        anglular_position_list.append(angular_position)
        angular_velocity_list.append(angular_velocity)

# Here a data frame of the particles data is generated
dframe = pd.DataFrame(data, columns=['pos', 'vel', 'time', 'pendulum', 'damping', 'Kinetic energy', 'Potential energy', 'Total energy'])

# This saves the data of the particles to an excel sheet
dframe.to_excel('dataframe.xlsx', sheet_name='new_sheet_name')

print('complete')
