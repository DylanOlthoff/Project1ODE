# Dylan Olthoff
# CST - 305
# Topic 1 Project 1: Visualize ODE with SciPy
# Dr. Ricardo Citro

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#  modeling after ram latency given by CL/MHz * 1000
# CL = latency
# MHz = data rate
def RAM(CL, MHz):
   MHz = 2500
   ddMHz = 1000/MHz # ODE relative to MHz
   return ddMHz

# initial conditions

p0 = 1

# timeline in seconds

t = np.linspace(0, 60)

#  solving the ODE

p = odeint(RAM,p0,t)
 # visualization of the project
print(t, p)
plt.plot(t,p)
plt.xlabel('time')
plt.ylabel('Time it takes for ram to access memory')
plt.show()