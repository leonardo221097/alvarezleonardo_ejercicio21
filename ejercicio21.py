import numpy as np
import matplotlib.pylab as plt
t=np.linspace(0,10,100)
y= np.sin(t)

plt.plot(t,y)
plt.savefig("seno.png")
plt.show()
 