# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 02:10:48 2022

@author: Alvaro
"""
import math
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
def percentil(per, datos):
    # Copiar la lista para no alterarla
    x = datos.copy()
    x.sort()

    n = len(x)
    rank = (per / 100.0) * (n - 1)
    rank_int = int(rank)
    rank_dec = rank % 1

    if rank_dec:
        p = x[rank_int] + rank_dec * (x[rank_int + 1] - x[rank_int])
    else:
        p = x[rank_int]

    return p

print("datos")
datoss = seleccion["age"]
print (datoss)

print(percentil(0.25, datoss))


