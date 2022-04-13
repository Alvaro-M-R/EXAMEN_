# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 03:52:41 2022

@author: Alvaro
"""

import numpy as np
from sklearn.impute import SimpleImputer
prepro = SimpleImputer(missing_values=np.nan, strategy="mean")
x1=np.array([
    [1,2,3],
    [4,np.nan,5],
    [np.nan,1,np.nan]])
x2=prepro.fit_transform(x1)
print(x2)