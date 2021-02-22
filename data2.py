import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('Iris.csv')
dataset = dataset.drop('Id',axis=1)

x = dataset.iloc[:,1:-1].values
y = dataset.iloc[:,-1].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
en = OneHotEncoder()
y = en.fit_transform(y.reshape(-1,1)).toarray()
iris1 = y[:,:1]
iris2 = y[:,1:2]
iris3 = y[:,2:3]
l = [] 
m = []
n = []
for i in range(len(iris1)):
    if(iris1[i][0] == 1):
        l.append(int(iris1[i][0]))
for h in range(len(l)):
    l[h] = 0
for j in range(len(iris2)):
    if(iris2[j][0] == 1):
        m.append(int(iris2[i][0]))
for h in range(len(m)):
    m[h] = 1
for i in range(len(iris3)):
    if(iris3[i][0] == 1):
        n.append(int(iris3[i][0]))
for h in range(len(n)):
    n[h] = 2
finalK = l+m+n
y = np.array(finalK)
from sklearn.cluster import KMeans

km = KMeans(n_clusters = 3, n_jobs = 4, random_state=21)
km.fit(x)

new_labels = km.labels_
# Plot the identified clusters and compare with the answers
fig, axes = plt.subplots(1, 2, figsize=(16,8))
axes[0].scatter(x[:, 0], x[:, 1], c=y, cmap='gist_rainbow',
edgecolor='k', s=150)
axes[1].scatter(x[:, 0], x[:, 1], c=new_labels, cmap='jet',
edgecolor='k', s=150)
axes[0].set_xlabel('Sepal length', fontsize=18)
axes[0].set_ylabel('Sepal width', fontsize=18)
axes[1].set_xlabel('Sepal length', fontsize=18)
axes[1].set_ylabel('Sepal width', fontsize=18)
axes[0].tick_params(direction='in', length=10, width=5, colors='k', labelsize=20)
axes[1].tick_params(direction='in', length=10, width=5, colors='k', labelsize=20)
axes[0].set_title('Actual', fontsize=18)
axes[1].set_title('Predicted', fontsize=18)