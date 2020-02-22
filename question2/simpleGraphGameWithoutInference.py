# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 14:10:49 2020

@author: Tanguy
"""

import networkx as nx
import random

def displayGraph(graph) :
    nx.draw(graph,with_labels=True, font_weight='bold')

n = 100 # Number of nodes

# Building graph with n non-connected nodes
G = nx.Graph()
for i in range(1,n+1) :
    G.add_node(i,value=0)

eligibleNodes = list(G.nodes)
allNodes = list(G.nodes)

for i in range(0,n):
    
    # Choose a node and remove it from the node list
    randomNode = random.choice(eligibleNodes)
    eligibleNodes.remove(randomNode)
    
    # List of all nodes with their values, current one (randomNode) removed
    nodeValues = list(G.nodes(data=True))
    nodeValues.remove((randomNode,G.node[randomNode]))
    
    # Get the higher value of all the other nodes
    higherValue = max(nodeValues,key=lambda item:item[1]['value'])[1]['value']

    # If the higher value is 0, we chose a random node in the other ones (it means that we have a fully non-connected graph)
    if higherValue == 0 :
        nodeToConnect = random.choice(nodeValues)[0]
        G.add_edge(randomNode,nodeToConnect)
        G.node[randomNode]['value'] = 1
        
        G.node[nodeToConnect]['value'] = 1

    else :
        # Make a list of all nodes with the higher value
        listOfMax = []
        for node in nodeValues :
            if node[1]['value'] == higherValue :
                listOfMax.append(node[0])
        
        # Random choose of one of the higher value nodes
        nodeToConnect = random.choice(listOfMax) 
    
        # If there isn't already an edge between the two nodes
        if G.has_edge(nodeToConnect,randomNode) == False :
            
            # Connect the selected node (randomNode) with a node that will maximize his value
            G.add_edge(randomNode,nodeToConnect)
            
            G.node[randomNode]['value'] += G.node[nodeToConnect]['value']
            
            G.node[nodeToConnect]['value'] += G.node[randomNode]['value']
            
    print(nodeToConnect,randomNode)
            
        

        
        

print(G.node[nodeToConnect])
displayGraph(G)







