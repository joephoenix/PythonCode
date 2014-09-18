import numpy as np;
import pylab as pl;

# use numpy to load the data contained in the file
data = np.loadtxt('fakedata.txt');

# plot the first column as x, and second column as yield
pl.plot(data[:,0], data[:,1], 'ro');

pl.xlabel('x');
pl.ylabel('y');

pl.xlim(0.0, 10.);

pl.show();