# -*- coding: utf-8 -*-
"""
@author: Alvaro
"""

from sklearn import tree
from sklearn import datasets as ds

iris = ds.load_iris()
print(iris)

x = iris.data
y = iris.target

print(x)
print(y)

clasificador = tree.DecisionTreeClassifier()
print(clasificador)
resultado=clasificador.fit(x,y)
xp=[[5.3, 3.7, 1.5, 0.2],
    [5. , 3.5, 1.3, 0.3],
    [4.5, 2.3, 1.3, 0.3],
    [5.,  3.3, 1.4, 0.2],
    [7.,  3.2, 4.7, 1.4],
    [6.4, 3.2, 4.5, 1.5]]
yp=clasificador.predict(xp)
print(yp)




