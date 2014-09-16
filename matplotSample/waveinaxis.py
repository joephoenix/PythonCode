# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FuncFormatter
import numpy as np

x = np.arange(0,4*np.pi, 0.01);
y = np.sin(x);

plt.figure(figsize=(8,4));
plt.plot(x,y);
ax = plt.gca();

def pi_formatter(x,pos):
   m = np.round(x / (np.pi / 4));
   n = 4;
   if m%2 == 0: m, n = m/2, n/2;
   if m%2 == 0: m, n = m/2, n/2;
   if m == 0: return "0";
   if m == 1 and n == 1: return "$\pi$";
   if n == 1 : return r"$%d \pi$" % m;
   if m == 1 : return r"$\frac{\pi}{%d}$" %n;
   return r"$\frac{%d \pi}{%d}$" % (m,n);
 
plt.ylim(-1.5,1.5);
plt.xlim(0,np.max(x));

plt.subplots_adjust(bottom = 0.15);

plt.grid();

ax.xaxis.set_major_locator(MultipleLocator(np.pi/4));

ax.xaxis.set_major_formatter(FuncFormatter(pi_formatter));

ax.xaxis.set_minor_locator(MultipleLocator(np.pi/20));

for tick in ax.xaxis.get_major_ticks():
    tick.label1.set_fontsize(16);
	
plt.show();