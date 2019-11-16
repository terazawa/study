#%%
import matplotlib.pyplot as plt
import numpy as np
from scipy import sparse
import pandas as pd
import mglearn
import seaborn as sns
sns.set_palette("tab10", n_colors=24)

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

#%%
from sklearn.datasets import load_iris
iris_dataset = load_iris()
print(iris_dataset)

#%%
print(iris_dataset.keys())

#%%
print(iris_dataset['DESCR'][:193])

#%%
print(iris_dataset['target_names'])

#%%
print(iris_dataset['feature_names'])

#%%
print(type(iris_dataset['data']))

#%%
print(iris_dataset['data'].shape)

#%%
print(iris_dataset['data'][:5])

#%%
print(type(iris_dataset['target']))

#%%
print(iris_dataset['target'].shape)

#%%
print(iris_dataset['target'])

#%%
X = iris_dataset['data']
y = iris_dataset['target']
print(f"X: {X.shape}")
print(f"y: {y.shape}")

#%%
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( X, y, random_state=0 )

#%%
print(f"X_train: {X_train.shape}")
print(f"X_test : {X_test.shape}")
print(f"y_train: {y_train.shape}")
print(f"y_test : {y_test.shape}")

#%%
iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
iris_dataframe

#%%
from pandas.plotting import scatter_matrix
grr = pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o',
hist_kwds={'bins': 20}, s=60, alpha=.8, cmap=mglearn.cm3)

#%%
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)

#%%
knn.fit(X_train, y_train)

#%%
X_new = np.array([[5, 2.9, 1, 0.2]])
print(X_new)

#%%
p_new = knn.predict(X_new)
print(iris_dataset['target_names'][p_new])

#%%
y_pred = knn.predict(X_test)
print(y_pred)

#%%
print(f"Test set score: {np.mean(y_pred == y_test):.2f}")

#%%
print(f"Test set score: {knn.score(X_test, y_test):.2f}")
