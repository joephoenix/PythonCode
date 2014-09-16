import numpy as np;

x = np.arange(0.0, 10., 1.);
y = x * x;

print 'x = ', x;
print 'y = ', y;

file = open('testdata.txt', 'w');

for i in range(len(x)):
   txt = str(x[i]) + '\t' + str(y[i]) + '\n';
   file.write(txt);

file.close();