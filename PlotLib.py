import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(0,5,11)
y=x**2
fig1= plt.figure();
axes=fig1.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_xlabel('X axis')
axes.set_ylabel('Y axis')
axes.set_title('Title')
plt.show()