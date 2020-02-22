# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 13:26:58 2019

@author: tangu
"""

import networkx as nx
import matplotlib.pyplot as plt

n = 100
pIteration = 100
probabilities = []
clusterSize = []
maxDegree = []

G = nx.binomial_graph(100,1)
nx.draw(G,with_labels=True, font_weight='bold')


for i in range(0,pIteration):
    probabilities.append([])
    clusterSize.append([])
    maxDegree.append([])
print(probabilities)
for i in range(0,100) :
    print(i)
    for tempP in range(0,pIteration) :
        p = tempP/(pIteration*10)
        probabilities[tempP].append(p)
        G = nx.binomial_graph(n,p)
        Gc = max(nx.connected_component_subgraphs(G), key=len)
        clusterSize[tempP].append(len(Gc.nodes()))
        maxDegree[tempP].append(max([d for n, d in G.degree()]))

finalProbabilities = []
finalClusterSizes = []
finalMaxDegrees = []
for i in range(0,len(probabilities)):
    finalProbabilities.append(sum(probabilities[i])/len(probabilities[i]))
    finalClusterSizes.append(sum(clusterSize[i])/len(clusterSize[i]))
    finalMaxDegrees.append(sum(maxDegree[i])/len(maxDegree[i]))


plt.plot(finalProbabilities, finalClusterSizes,label="Cluster size")
plt.plot(finalProbabilities, finalMaxDegrees, label="Max node degree")
plt.grid(True)
plt.legend()
plt.show()




