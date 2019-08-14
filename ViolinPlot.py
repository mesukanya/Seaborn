import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt

df= sb.load_dataset('tips')

sb.violinplot(x = "day", y = "total_bill",  data = df)
plt.show()


