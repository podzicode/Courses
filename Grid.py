import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset('tips')
flight=sns.load_dataset('flights')
iris=sns.load_dataset('iris')
g=sns.PairGrid(iris)
#g=sns.FacetGrid(data=tips,row='smoker',col='time')
g.map(plt.hist)
plt.show()