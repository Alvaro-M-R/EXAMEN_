# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 18:11:40 2022

@author: Alvaro
"""

from kanren import run, var , eq, Relation, facts
a = var()
b = var()
#print(run(1,a,eq(a,5)))
#print(run(1,b,eq(b,6)))
#print(a)
#print(b._id)

padre = Relation()
hermanos = Relation()
tios= Relation()
primos=Relation()
abuelo=Relation()

facts(padre, ("papa", "hijo1"),("papa", "hijo2"),("abuelo", "papa"),
      ("abuelo", "tio1"),("abuelo","tio2"),("tio1","primo1_1"),
      ("tio1","primo1_2"),("tio2","primo2_1"))

facts(hermanos, ("papa","tio1"),("papa","tio2"),("tio1","tio2"),
      ("hijo1","hijo2"),("primo1_1","primo1_2"))

facts(tios,("hijo1","tio1"),("hijo1","tio2"),("hijo2","tio1"),("hijo2","tio2"),
      ("primo1_1","papa"),("primo1_1","tio2"),("primo1_2","papa"),("primo1_2","tio2"),
      ("primo2_1","papa"),("primo2_1","tio1"))

facts(primos, ("primo1_1","hijo1"),("primo1_1","hijo2"),("primo1_1","primo2_1"),
      ("primo1_2","hijo1"),("primo1_2","hijo2"),("primo1_2","primo2_1"),
      ("hijo1","primo1_1"),("hijo1","primo2.1"),("hijo1","primo1_2"),
      ("hijo2","primo1_1"),("hijo2","primo2.1"),("hijo2","primo1_2"),
      ("primo2_1","primo1_1"),("primo2_1","primo1_2"),("primo2_1","hijo1"),("primo2_1","hijo2"))

facts(abuelo, ("abuelo","hijo1"),("abuelo","hijo2"),("abuelo","primo2_1"),("abuelo","primo1_1"),
      ("abuelo","primo1_2"))


print(padre.facts)
print("----------------")
print(run(4,a,padre(a,"hijo1")))
print("----------------")
print(run(6,b,primos("primo1_1",b)))
print("----------------")
print(run(6,b,hermanos("primo2_1",b)))
print("----------------")
print(run(6,b,abuelo("abuelo",b)))


















