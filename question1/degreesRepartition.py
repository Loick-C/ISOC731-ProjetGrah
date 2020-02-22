# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 16:43:07 2019

@author: tangu
"""

import networkx as nx
import matplotlib.pyplot as plt
import collections
import pandas as pd
import numpy as np
n=1000 #nombre de noeud
pIteration = 101 #parcours des proba
iteration = 100 #nombre d'arbres
probabilities = []
degrees = []
proba=np.arange(0,pIteration/100,0.01)
#création des listes
for i in range(0,pIteration):
    probabilities.append([])
    degrees.append([])

#boucle sur les arbres
for i in range(0,iteration) :
    print(i)
    #pour chaque arbre on parcours nos proba
    for tempP in range(0,pIteration) :
        #p est la proba 
        p = tempP/100
        probabilities[tempP].append(p)
        
        #création de l'arbre
        G = nx.binomial_graph(n,p)
        #on s'occupe des dégrés
        degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
        degreeCount = collections.Counter(degree_sequence)
        degrees[tempP].append(degreeCount)

#on regroupe les résultats de chaque arbres
counter=[]
for i in range(0,len(degrees)) : 
    collectionSum=collections.Counter()
    for j in range(0,len(degrees[i])):
        collectionSum = collectionSum + degrees[i][j]
    counter.append(collectionSum)
    sums = dict(collectionSum)
#    means = {k: sums[k] / float((k in degrees[i][0]) + (k in degrees[i][1])) for k in sums}
means=list()
for i in range(len(counter)) : 
    means.append(counter[i])
    for key,value in means[i].items() : 
        means[i][key]=means[i][key]/iteration

#calcul de la moyenne de degres pour chaque noeud pour tous les arbres   
df = pd.DataFrame(means,index=proba)
df = df.transpose()
import seaborn as sns; sns.set()

#cmap = sns.cubehelix_palette(as_cmap=True, light=.9)
#cmap.set_under(".5")
ax= sns.heatmap(df, cmap=sns.color_palette("RdBu_r"), mask=df.isnull())
ax.set_ylabel('Degrés')
ax.set_xlabel('p')

#heatmap 
    
    
    
    