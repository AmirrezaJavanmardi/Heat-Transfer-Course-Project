import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math 
L = 0.11 
D = 0.01 
r = D / 2
A_c = ((math.pi) * D **2) / 4
T_b  = 450 
T_inf = 25 + 273.15
P = math.pi * D 
theta_b = T_b - T_inf 
k = [5, 50, 500]
h = [1, 10, 100]
m = []
for i in k:
    for j in h:
        m.append((4 * j /(i * D)) ** 0.5)

def theta(parameter, x, th_b, l ):
    theta_x = th_b * (math.cosh(parameter*(l - x))/math.cosh(parameter * l))
    return theta_x

x = np.arange(0, 110 , 0.005)
Ts =[[],[],[],[],[],[],[],[],[]]
thetas =[[],[],[],[],[],[],[],[],[]]
ratios =[[],[],[],[],[],[],[],[],[]]
f = 0 
for M in m:
    for j in x :
        Ts[f].append(theta(M, j/1000 , theta_b, L) + T_inf)
        thetas[f].append(theta(M, j/1000 , theta_b, L))
        ratios[f].append(theta(M, j/1000 , theta_b, L)/theta_b)
    f += 1

####################################################################
plt.figure()
plt.plot(x, Ts[0], label='k = 5 & h = 1', linewidth=3)
plt.plot(x, Ts[1], label='k = 5 & h = 10', linewidth=3)
plt.plot(x, Ts[2], label='k = 5 & h = 100', linewidth=3)
plt.axhline(y=0, color='black', linestyle='-')
plt.axhline(y=450, color='r', label='T_b', linestyle='--', linewidth=1)
plt.axhline(y=T_inf, color='r', label='T_inf = 298.15 K', linestyle='dotted', linewidth=1)
plt.axvline(x=0, color='black', linestyle='-')
plt.xlim(0, 115)     
plt.ylim(250, 460)
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(25))
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(10))
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth=0.75, color='gray', alpha=0.7)
plt.grid(which='minor', linestyle=':', linewidth=0.5, color='lightgray', alpha=0.5)
plt.legend()
plt.xlabel('x [mm]')
plt.ylabel('T [k]') 
plt.title('temp distribution for k = 5')
plt.show()
####################################################################
plt.figure()
plt.plot(x, Ts[3], label='k = 50 & h = 1', linewidth=3)
plt.plot(x, Ts[4], label='k = 50 & h = 10', linewidth=3)
plt.plot(x, Ts[5], label='k = 50 & h = 100', linewidth=3)
plt.axhline(y=0, color='black', linestyle='-')
plt.axhline(y=450, color='r', label='T_b', linestyle='--', linewidth=1)
plt.axhline(y=T_inf, color='r', label='T_inf = 298.15 K', linestyle='dotted', linewidth=1)
plt.axvline(x=0, color='black', linestyle='-')
plt.xlim(0, 115)     
plt.ylim(250, 460)
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(25))
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(10))
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth=0.75, color='gray', alpha=0.7)
plt.grid(which='minor', linestyle=':', linewidth=0.5, color='lightgray', alpha=0.5)
plt.legend()
plt.xlabel('x [mm]')
plt.ylabel('T [k]') 
plt.title('temp distribution for k = 50')
plt.show()
####################################################################
plt.figure()
plt.plot(x, Ts[6], label='k = 50 & h = 1', linewidth=3)
plt.plot(x, Ts[7], label='k = 50 & h = 10', linewidth=3)
plt.plot(x, Ts[8], label='k = 50 & h = 100', linewidth=3)
plt.axhline(y=0, color='black', linestyle='-')
plt.axhline(y=450, color='r', label='T_b', linestyle='--', linewidth=1)
plt.axhline(y=T_inf, color='r', label='T_inf = 298.15 K', linestyle='dotted', linewidth=1)
plt.axvline(x=0, color='black', linestyle='-')
plt.xlim(0, 115)     
plt.ylim(250, 460)
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(25))
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(10))
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth=0.75, color='gray', alpha=0.7)
plt.grid(which='minor', linestyle=':', linewidth=0.5, color='lightgray', alpha=0.5)
plt.legend()
plt.xlabel('x [mm]')
plt.ylabel('T [k]') 
plt.title('temp distribution for k = 500')
plt.show()
####################################################################
plt.figure()
plt.plot(x, ratios[0], label='k = 5 & h = 1', linewidth=3)
plt.plot(x, ratios[1], label='k = 5 & h = 10', linewidth=3)
plt.plot(x, ratios[2], label='k = 5 & h = 100', linewidth=3)
plt.axhline(y=0, color='black', linestyle='-')
plt.axvline(x=0, color='black', linestyle='-')
plt.xlim(0, 115)     
plt.ylim(-0.05, 1)
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.05))
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(10))
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth=0.75, color='gray', alpha=0.7)
plt.grid(which='minor', linestyle=':', linewidth=0.5, color='lightgray', alpha=0.5)
plt.legend()
plt.xlabel('x [mm]')
plt.ylabel('theta/theta_b') 
plt.title('theta/theta_b')
plt.show()
####################################################################
plt.figure()
plt.plot(x, ratios[3], label='k = 5 & h = 1', linewidth=3)
plt.plot(x, ratios[4], label='k = 5 & h = 10', linewidth=3)
plt.plot(x, ratios[5], label='k = 5 & h = 100', linewidth=3)
plt.axhline(y=0, color='black', linestyle='-')
plt.axvline(x=0, color='black', linestyle='-')
plt.xlim(0, 115)     
plt.ylim(0, 1)
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.05))
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(10))
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth=0.75, color='gray', alpha=0.7)
plt.grid(which='minor', linestyle=':', linewidth=0.5, color='lightgray', alpha=0.5)
plt.legend()
plt.xlabel('x [mm]')
plt.ylabel('theta/theta_b') 
plt.title('theta/theta_b')
plt.show()
####################################################################
plt.figure()
plt.plot(x, ratios[6], label='k = 5 & h = 1', linewidth=3)
plt.plot(x, ratios[7], label='k = 5 & h = 10', linewidth=3)
plt.plot(x, ratios[8], label='k = 5 & h = 100', linewidth=3)
plt.axhline(y=0, color='black', linestyle='-')
plt.axvline(x=0, color='black', linestyle='-')
plt.xlim(0, 115)     
plt.ylim(0, 1)
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.05))
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(10))
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth=0.75, color='gray', alpha=0.7)
plt.grid(which='minor', linestyle=':', linewidth=0.5, color='lightgray', alpha=0.5)
plt.legend()
plt.xlabel('x [mm]')
plt.ylabel('theta/theta_b') 
plt.title('theta/theta_b')
plt.show()
####################################################################