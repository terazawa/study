#%%
import matplotlib.pyplot as plt
import numpy as np
from scipy import sparse
import pandas as pd
import mglearn

#%%
x = np.array([[1, 2, 3], [4, 5, 6]])
print(x)

#%%
eye = np.eye(4)
print(eye)

#%%
sparse_matrix = sparse.csr_matrix(eye)
print(sparse_matrix)

#%%
data = np.ones(4)
print(data)
row_indices = np.arange(4)
print(row_indices)
col_indices = np.arange(4)
eye_coo = sparse.coo_matrix((data, (row_indices, col_indices)))
print(eye_coo)

#%%
x = np.linspace(-10, 10, 100)
y = np.sin(x)
plt.plot(x, y, marker="x")

#%%
data = {
    'Name': ["John", "Anna", "Peter", "Linda"],
    'Location': ["New York", "Paris", "Berlin", "London"],
    'Age': [24, 13, 53, 33]
}
data_pandas = pd.DataFrame(data)
data_pandas

#%%
data_pandas[data_pandas.Age > 30]
