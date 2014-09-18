import matplotlib.pyplot as plt

x = arange(1, 1000, 1);
r = -2;
c = 5;
y = [5*(a**r) for a in xrange]

fig = plt.figure();

ax = fig.add_subplot(111);
#使用laText输入数学公式，需要软件排版处理
ax = loglog(x,y,label=r"");

ax.legend();
ax.set_xlabel(r"x");
ax.set_ylabel(r"y");