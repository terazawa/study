#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mglearn
import seaborn as sns
sns.set_palette("tab10", n_colors=24)
import altair as alt

#%%
X, y = mglearn.datasets.make_forge()
mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
plt.legend(["Class 0", "Class 1"])
plt.xlabel("First feature")
plt.ylabel("Second feature")
print(f"X.shape: {X.shape}")

#%%
X, y = mglearn.datasets.make_wave(n_samples=40)
plt.plot(X, y, 'o')
plt.ylim(-3, 3)
plt.xlabel("Feature")
plt.ylabel("Target")

#%%
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
print(f"cancer.keys(): \n{cancer.keys()}")

#%%
print(f"Shape of cancer data: {cancer.data.shape}")

#%%
dic = {n: v for n, v in zip(cancer.target_names, np.bincount(cancer.target))}
print(f"Sample counts per class:\n{dic}")

#%%
print(f"Feature names:\n{cancer.feature_names}")

#%%
from sklearn.datasets import load_boston
boston = load_boston()
print(f"Data shape: {boston.data.shape}")
print(boston.DESCR)

#%%
X, y = mglearn.datasets.load_extended_boston()
print(f"X.shape: {X.shape}")

#%%
mglearn.plots.plot_knn_classification(n_neighbors=1)

#%%
mglearn.plots.plot_knn_classification(n_neighbors=3)

#%%
mglearn.plots.plot_knn_classification(n_neighbors=5)

#%%
# separate datasets
from sklearn.model_selection import train_test_split
X, y = mglearn.datasets.make_forge()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

#%%
print(X_train)
print(type(X_train))
print(X_train[:,0])
plt.scatter(X_train[:,0], X_train[:,1])

#%%
df = pd.DataFrame(X_train, columns=['x1', 'x2'])
alt.Chart(df).mark_point().encode(
    x=alt.X('x1', scale=alt.Scale(zero=False)),
    y='x2',
)

