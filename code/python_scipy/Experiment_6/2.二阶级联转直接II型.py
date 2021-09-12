import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

a=0.75
sos=[[a*1,a*9*0.1,0,1,-0.6,0],[1,0.9*0.1,0.36,1,-0.7,0.49]]
b,a = signal.sos2tf(sos)
print(b)
print(a)
