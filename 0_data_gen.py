"""
generates example dataset
"""
import numpy as np
import pandas as pd

N = 1000
D = 1
X = np.random.randn(N, D)
Y = X ** 3 + np.random.randn(N,D) * 0.1
data = np.hstack([X, Y])
df = pd.DataFrame(data, columns=['X', 'Y'])
df.to_csv('example_data.csv', index=None)
