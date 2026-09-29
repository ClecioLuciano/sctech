import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Titanic.csv')

sns.boxplot(x=df['Age'])
plt.show()