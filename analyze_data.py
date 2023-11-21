import pandas as pd

df = pd.read_csv('your_dataset.csv')

df.head()

summary_stats = df.describe()
df_cleaned = df[df['column_name'] > value]
import matplotlib.pyplot as plt
df['column_name'].hist()
plt.title('Histogram of Column')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()