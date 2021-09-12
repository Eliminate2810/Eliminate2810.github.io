import matplotlib.pyplot as plt
from scipy import signal

c=99
b=[6,1,-4,c]
a=[8,-10,7,-2]
sos = signal.tf2sos(b, a)
print(sos)