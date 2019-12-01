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
features = ['x1', 'x2']
df = pd.DataFrame(X, columns=features)
df['y'] = y
df_train, df_test = train_test_split(df, random_state=0)

#%%
df_train

#%%
df_test

#%%
alt.Chart(df_train).mark_point().encode(
    x=alt.X('x1', scale=alt.Scale(zero=False)),
    y='x2',
    color='y:N'
)

#%%
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=3)

#%%
clf.fit(df_train[features], df_train.y)

#%%
print(f"Test set predicctions: {clf.predict(df_test[features])}")

#%%
print(f"Test set accuracy: {clf.score(df_test[features], df_test.y):.2f}")

#%%
df_train['predict'] = clf.predict(df_train[features])
df_test['predict'] = clf.predict(df_test[features])

#%%
chart_train = alt.Chart(df_train).mark_point(filled=True).encode(
    x=alt.X('x1', scale=alt.Scale(zero=False)),
    y='x2',
    color='y:N',
    shape='predict:N'
)
chart_test = alt.Chart(df_test).mark_point(filled=False).encode(
    x=alt.X('x1', scale=alt.Scale(zero=False)),
    y='x2',
    color='y:N',
    shape='predict:N'
)
chart_train + chart_test

#%%
fig, axes = plt.subplots(1, 3, figsize=(10, 3))
for n_neighbors, ax in zip([1, 3, 9], axes):
    clf = KNeighborsClassifier(n_neighbors=n_neighbors).fit(X, y)
    mglearn.plots.plot_2d_separator(clf, X, fill=True, eps=0.5, ax=ax, alpha=0.4)
    mglearn.discrete_scatter(X[:, 0], X[:, 1], y, ax=ax)
    ax.set_title(f"{n_neighbors} neighbors")
    ax.set_xlabel("feature 0")
    ax.set_ylabel("feature 1")
axes[0].legend(loc=3)

#%%
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, 
    cancer.target, 
    stratify=cancer.target, random_state=66)

df = pd.DataFrame(cancer.data, columns=cancer.feature_names)
df

#%%
training_accuracy = []
test_accuracy = []
neighbors_settings = range(1, 11)
for n_neighbors in neighbors_settings:
    clf = KNeighborsClassifier(n_neighbors=n_neighbors)
    clf.fit(X_train, y_train)
    training_accuracy.append(clf.score(X_train, y_train))
    test_accuracy.append(clf.score(X_test, y_test))
plt.plot(neighbors_settings, training_accuracy, label='traing accuracy')
plt.plot(neighbors_settings, test_accuracy, label='test accuracy')
plt.ylabel('Accuracy')
plt.xlabel('n_neighbors')
plt.legend()

#%%
mglearn.plots.plot_knn_regression(n_neighbors=1)
mglearn.plots.plot_knn_regression(n_neighbors=3)

#%%
from sklearn.neighbors import KNeighborsRegressor
X, y = mglearn.datasets.make_wave(n_samples=40)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
reg = KNeighborsRegressor(n_neighbors=3)
reg.fit(X_train, y_train)

#%%
print(f"Test set predictions:\n{reg.predict(X_test)}")

#%%
print(f"Test set R^2: {reg.score(X_test, y_test):.2f}")

#%%
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
line = np.linspace(-3, 3, 1000).reshape(-1, 1)
for n_neighbors, ax in zip([1, 3, 9], axes):
    reg = KNeighborsRegressor(n_neighbors=n_neighbors)
    reg.fit(X_train, y_train)
    ax.plot(line, reg.predict(line))
    ax.plot(X_train, y_train, '^', c=mglearn.cm2(0), markersize=8)
    ax.plot(X_test, y_test, 'v', c=mglearn.cm2(1), markersize=8)
    ax.set_title(f"{n_neighbors} neighbor(s)\n train score: {reg.score(X_train, y_train):.2f} test score: {reg.score(X_test, y_test):.2f}")
    ax.set_xlabel("Feature")
    ax.set_ylabel("Target")
axes[0].legend(["Model predictions", "Training data/target", "Test data/target"], loc="best")

