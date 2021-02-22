import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("student_scores.csv")

X = dataset.iloc[:,:-1]
x = dataset.iloc[:, :-1].values
y =  dataset.iloc[:, -1].values


from sklearn.linear_model import  LinearRegression
reg = LinearRegression()
reg.fit(x,y)


yPredict = reg.predict([[0]])

plt.scatter(X,y)