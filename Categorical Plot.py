import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset('tips')
#sns.barplot(x='sex',y='total_bill',data=tips,palette='pastel')
#sns.boxplot(x='day',y='total_bill',data=tips,hue='sex',palette='pastel')
#sns.violinplot(x='day',y='total_bill',data=tips,palette='pastel')
#sns.stripplot(x='day',y='total_bill',data=tips,hue='sex',palette='pastel')
#sns.swarmplot(x='day',y='total_bill',data=tips,hue='sex',color='black')
plt.show()