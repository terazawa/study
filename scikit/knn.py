#%%
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import mglearn
sns.set_palette("tab10", n_colors=24)

#%%
from sklearn.datasets import load_iris
iris_dataset = load_iris()
X = iris_dataset['data']
y = iris_dataset['target']
print(f"X: {X.shape}")
print(f"y: {y.shape}")

#%%
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( X, y, random_state=0 )
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
p_new
