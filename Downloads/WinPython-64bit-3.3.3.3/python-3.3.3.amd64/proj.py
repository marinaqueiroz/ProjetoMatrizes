# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 23:04:14 2014

@author: Marina
"""
import random
import numpy as np
import numpy
import time

tam=10
ordem=3
ordemQuadrada=ordem**2
listaVetores=[]
m=[]
m2=[]
m5=[]
aux=0
aux2=[]
matriz=[]

for i in range(ordemQuadrada):
    lista=np.array(np.random.randn(tam))
    listaVetores.append(lista)
    del (lista)
#print(listaVetores)
#print(len(listaVetores))
#print("*****"+"****************************************************************")
for j in range(len(listaVetores[0])):
    numerosSorteados = []
    d=random.randint(0,len(listaVetores[0])-1)
    numerosSorteados.append(d)
    while(d in numerosSorteados):
        d=random.randint(0,len(listaVetores[0])-1)
    
    for k in range(len(listaVetores)):
        m.append(listaVetores[k][d])
del(listaVetores)

#print("tam",len(m))
#print("m",m)
#print("*****"+"****************************************************************")
while(len(m2)<tam):
    m3=m[0:ordemQuadrada]
    del m[0:ordemQuadrada]
    m2.append(m3)
    

#print("m2",m2)
#print("okkk",len(m2))
#print("*****"+"****************************************************************")
while(aux!=ordem):
   for l in range(tam):
      m4=m2[l][0:ordem]
      del m2[l][0:ordem]
      m5.append(m4)
   aux+=1
del(m2)
#print("m5",(m5))
#print("okkk",len(m5))
#print("*****"+"****************************************************************")
for n in range(tam):
    m6=[m5[0]]+[m5[1]]
    del m5[:1]
    aux2.append(m6)
#print(aux2)
#print(len(aux2))   
#print("*****"+"****************************************************************")

for i in range(tam):
    x=numpy.matrix(aux2[i])
    matriz.append(x)
del(aux2)
print(matriz)
print(len(matriz))
print ("tempo=",time.clock())
    


    
         
        
    
    
        

            

    




           









