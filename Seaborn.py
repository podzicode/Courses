import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset('tips')
tips.head()
#sns.distplot(tips['total_bill'],kde=False)
sns.jointplot(x='total_bill',y='tip',data=tips)
plt.show()