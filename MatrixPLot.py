import seaborn as sns
import matplotlib.pyplot as plt

#tips=sns.load_dataset('tips')
flights=sns.load_dataset('flights')
flights.head()
fp=flights.pivot_table(index='month',columns='year',values='passengers')
#sns.heatmap(fp,cmap='coolwarm')
sns.clustermap(fp,cmap='coolwarm',standard_scale=1)
plt.show()