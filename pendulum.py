#imports
import random as rnd 
import numpy as np

class Pendulum():
    '''
    A class which produces pendulums giving taking in a range
    of atributes; length, mass, damping, initial position 
    and initial angular velocity.
    '''
    def __init__(self, length, mass, damping, y_0):
        self.length = length # length of the pendulum string (infinetly taught and massless)
        self.mass = mass # mass at the end of the pendulum
        self.damping = damping # damping coefficinet 'b'
        self.y_0 = y_0 # vector of inital position and angular velocity
        self.g = 9.81

    def differential1(self, y):
        '''
        This function splits the second order ODE into two
        first order ODEs, by solving the differential
        equation: 

        dtheta2/d2t = -(g/l)sin(theta) - (b/m)dtheta/dt

        The angular position of the pendulum can be found for any
        time if these coupled ODEs are applied to a numerical
        method solving coupled ODEs.
        '''
        diff1 = y[1]
        diff2 = -(self.g/self.length)*np.sin(y[0]) - ((self.damping/self.mass)*y[1])
        return np.array([diff1, diff2])

    def kinetic_energy(self, yn):
        '''
        This functions returns the kinetic energy of the pendulum
        system for each position in time, using the equation:
        Ek = 1/2m(dtheta/dt)^2
        '''
        Ek = 0.5*(self.mass)*((self.differential1(yn)[0])**2)
        Ek = abs(Ek)
        return Ek 

    def potential_energy(self, yn):
        '''
        Function that produces potential energy of the pendulum
        system using the equation: 1/2mw^2theta^2
        This takes in the mass and the value of theta to calculate
        the potential.
        '''
        # w is the angular frequency of the oscillator without damping
        w = (self.g/self.length)**(1/2)
        w2 = w**2
        x2 = (yn[0]**2)
        Ep = 0.5*self.mass*w2*x2
        Ep = abs(Ep)
        return Ep

    def RK4_method(self, dt, yn):
        '''
        RK4 method for solving coupled ODEs, this takes in two linked ODEs
        and solves them for a spercific instance. After a second order
        ODE is split into two first order this function can be used to
        solve it.
        '''
        k1 = self.differential1((yn))
        k2 = self.differential1((yn + (1/2)*k1*dt))
        k3 = self.differential1((yn + (1/2)*k2*dt))
        k4 = self.differential1((yn + (1/2)*k3*dt))
        new_y = yn + (1.0/6.0)*(k1 + 2.0*k2 + 2.0*k3 + k4)*dt
        return new_y

    def ralston_method(self, dt, yn):
        '''
        Ralston method for solving coupled ODEs, takes in coupled ODEs and solves
        them 
        '''
        k1 = self.differential1(yn)
        k2 = self.differential1(yn[0]+(2/3)*k1[0]*dt, yn[1]+(2/3)*k1[1]*dt)
        new_y = [yn[0] + ((1/4)*k1[0] + (3/4)*k2[0])*dt, yn[1] + ((1/4)*k1[1]
        + (3/4)*k2[1])*dt]
        return new_y

    def forward_euler_method(self, dt, yn):
        '''
        The forward euler method, the most simple method for iteratively
        solving ODEs
        '''
        new_y = yn + self.differential1(yn*dt)
        return new_y