import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#x1=(n+2)R_6(n) x2=[2,4,5,3]

def R(n):
    x=np.arange(20+n)
    x[:n]=1
    x[n:]=0
    return x

def circonv(x1,x2,L):
    #把x1,x2转换成标准长度
    xt1=np.arange(L)
    xt2=np.arange(L)
    if len(x1)<L:
        for i in range (0, len(x1)):
            xt1[i]=x1[i]
        for i in range (len(x1),L):
            xt1[i]=0
    elif len(x1)>L:
        for i in range (0, L):
            xt1[i]=x1[i]
    if len(x2)<L:
        for i in range (0, len(x2)):
            xt2[i]=x2[i]
        for i in range (len(x2),L):
            xt2[i]=0
    elif len(x2)>L:
        for i in range (0, L):
            xt2[i]=x2[i]
#对x2圆周移位与x1矩阵乘法
    #对xt2翻褶+圆周右移1
    xt2 = np.flipud(xt2)
    xt2 = np.roll(xt2,1)    
    #构造x2L阶方阵
    x2L=np.arange(L*L).reshape(L,L)
    for i in range (0,L):                #i行j列
        for j in range (0,L):
            x2L[i,j]=xt2[j]
        xt2 = np.roll(xt2,1)
    #矩阵乘法
    x1Lx2=np.dot(x2L,xt1)
    return x1Lx2    
        
a=9
L=6+a
nmax=20
n=np.arange(nmax)
x1=(n+2)*R(6)[n]
x2=[2,4,5,3]

x1Lx2 = circonv(x1,x2,L)
#上圆周卷积x1Lx2，y线性卷积
y = signal.convolve(x1, x2)

Ln1=np.arange(L)
Ln2=np.arange(6*len(x2)-1)
plt.subplot(211)
plt.title('6+9点圆周卷积')
plt.stem(Ln1,x1Lx2,'b')
plt.subplot(212)
plt.title('线性卷积')
plt.stem(Ln2,y,'g')
plt.show()