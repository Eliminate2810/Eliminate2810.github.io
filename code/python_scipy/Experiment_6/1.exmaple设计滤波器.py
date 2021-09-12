import matplotlib.pyplot as plt
from scipy import signal

sos = signal.ellip(13, 0.009, 80, 0.05, output='sos')#滤波器顺序，通带最小增益，阻带最大衰减，Wn是角频率
print(sos)
x = signal.unit_impulse(700)
y_sos = signal.sosfilt(sos, x)
plt.plot(y_sos, 'k', label='SOS')
plt.show()

#b,a为直接二型的分子分母数组
#sos是二阶级联型  分别表示分子，分母系数                      [ 1.    2.6916986   0.      1.   -0.75     0.5  ]
#r,p,k是一阶并联型  分别表示各级分子系数，极点，常数