import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
tips=sns.load_dataset('tips')
#sns.set_style('darkgrid')
#sns.countplot(x='sex',data=tips)
#sns.set_context('poster',font_scale=3)
#sns.despine(left=True,bottom=True)
plt.show()
plt.boxplot