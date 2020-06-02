
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,6,0.1)
y = np.sin(x)
c = np.cos(x)
plt.plot(x,y,label="sin")
plt.plot(x,c,label="cos",linestyle="-")
plt.xlabel('x')
plt.ylabel('y')
plt.title('sin&cos')
plt.show()