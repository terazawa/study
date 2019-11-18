#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mglearn
import seaborn as sns
sns.set_palette("tab10", n_colors=24)

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
