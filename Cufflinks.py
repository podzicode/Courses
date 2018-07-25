import numpy as np
import pandas as pd
from pylab import *
import matplotlib.pyplot as plt
import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode,plot,iplot
#init_notebook_mode(connected=True)
cf.go_offline()
#DATA
df=pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
df.head()
df2=pd.DataFrame({'Category':['A','B','C'],'Values':[32,43,50]})
df2.head()
plt.interactive(True)
#fig=df.plot()
df.iplot()
plt.show()