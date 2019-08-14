import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('tips')
sb.swarmplot(x = "size", y = "total_bill", data = df)
plt.show()


dt = sb.load_dataset('tips')
sb.swarmplot(x = "day", y = "total_bill", data = dt)
plt.show()