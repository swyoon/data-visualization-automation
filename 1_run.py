# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

data_file = 'example_data.csv' 
print(f'reading data from {data_file}...')
df = pd.read_csv(data_file)

print(f'data read successfully. Displaying top 5 rows')
print(df.head(5))

plt.plot(df['X'], df['Y'], '.')
a, b = np.polyfit(df['X'], df['Y'], deg=1)
x_min = df['X'].min()
x_max = df['X'].max()
# plt.figure()
plt.plot([x_min, x_max], [x_min * a + b, x_max * a + b], '-')
plt.savefig('result_figure.pdf', bbox_inches='tight')

