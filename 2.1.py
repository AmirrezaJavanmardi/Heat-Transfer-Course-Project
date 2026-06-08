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

def I0(x):
    a = (1 + x**2/4 + x**4/64 + x**6/2304 + x**8/147456 + x**10/14745600 + x**12/2123366400 + x**14/406610329600 + x**16/99179645337600 + x**18/29686813327974400)
    return a

def I1(x):
    a = (x/2 + x**3/16 + x**5/384 + x**7/18432 + x**9/1474560 + x**11/176947200 + x**13/29727129600 + x**15/6585032294400 + x**17/1880240926924800 + x**19/676886733692928000) 
    return a

def I2(x):
    a = (x**2/8 + x**4/96 + x**6/3072 + x**8/184320 + x**10/17694720 + x**12/2477260800 + x**14/474834739200 + x**16/118530581299200 + x**18/37604818538496000 + x**20/14780389842862080000)
    return a

def theta(parameter, x, th_b, l ):
    theta_x = th_b * (I1(2*parameter*l*(1 - x/l)**0.5)) / (I1(2*parameter*l) * (1 - x/l)**0.5)
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