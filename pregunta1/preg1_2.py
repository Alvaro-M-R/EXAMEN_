# -*- coding: utf-8 -*-
"""
@author: Alvaro
"""

import numpy as np
import pandas as pd

ckd = pd.read_csv("ckd2.csv",sep=",")
print (ckd)
print("*************************************")
print(ckd.head)

colnumericas = []
for c in ckd.columns:
    t = str(ckd[c].dtype)
    if "int" in t or "float" in t:
        colnumericas.append(c)
colnumericas
print(colnumericas)
seleccion = ckd[["age", "bp", "sg", "al", "su", "bgr", "bu", "sc", "sod", "pot", "hemo", 
                 "pcv", "wbcc", "rbcc"]]

print(seleccion)


#ckd2=ckd._get_numeric_data()
#print("----------ckd2------------")
#print(ckd2)
print("-----pandas----------")
print(seleccion.quantile(0.25 , axis=0))
print("----------50---------")
print(seleccion.quantile(0.50 , axis=0))
print("-----------Primer cuartil-----------")
print("age: ",np.percentile(seleccion["age"],25))
print("bp: ",np.percentile(seleccion["bp"],25))
print("sg: ",np.percentile(seleccion["sg"],25))
print("al: ",np.percentile(seleccion["al"],25))
print("su: ",np.percentile(seleccion["su"],25))
print("bgr: ",np.percentile(seleccion["bgr"],25))
print("bu: ",np.percentile(seleccion["bu"],25))
print("sc: ",np.percentile(seleccion["sc"],25))
print("sod: ",np.percentile(seleccion["sod"],25))
print("pot: ",np.percentile(seleccion["pot"],25))
print("hemo: ",np.percentile(seleccion["hemo"],25))
print("pcv: ",np.percentile(seleccion["pcv"],25))
print("wbcc: ",np.percentile(seleccion["wbcc"],25))
print("rbcc: ",np.percentile(seleccion["rbcc"],25))

print("-----------Percentil 50-----------")
print("age: ",np.percentile(seleccion["age"],50))
print("bp: ",np.percentile(seleccion["bp"],50))
print("sg: ",np.percentile(seleccion["sg"],50))
print("al: ",np.percentile(seleccion["al"],50))
print("su: ",np.percentile(seleccion["su"],50))
print("bgr: ",np.percentile(seleccion["bgr"],50))
print("bu: ",np.percentile(seleccion["bu"],50))
print("sc: ",np.percentile(seleccion["sc"],50))
print("sod: ",np.percentile(seleccion["sod"],50))
print("pot: ",np.percentile(seleccion["pot"],50))
print("hemo: ",np.percentile(seleccion["hemo"],50))
print("pcv: ",np.percentile(seleccion["pcv"],50))
print("wbcc: ",np.percentile(seleccion["wbcc"],50))
print("rbcc: ",np.percentile(seleccion["rbcc"],50))








#seleccion = ckd.select_dtypes(include = ["number"])
#print(seleccion.head())
#print("*************************************")

"""print(ckd["class"])
print("*****************************************")
ckdcolumna=ckd["age"]
print(ckdcolumna.loc[ckdcolumna==73].sum())
print("*****************************************")
#print(np.percentile(ckd,25), axis=0)for column in df:
for column in ckd:  
    print(ckd[column].values)"""
