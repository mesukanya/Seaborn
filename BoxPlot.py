import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt

df= sb.load_dataset('iris')

sb.boxplot(x = "species", y = "petal_length",  data = df)
plt.show()



df= sb.load_dataset('tips')

sb.boxplot(x = "smoker", y = "total_bill",  data = df)
plt.show()