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
    G.add_node(i,realValue=0)

eligibleNodes = list(G.nodes)
allNodes = list(G.nodes)

for i in range(0,100):
    
    # Choose a node and remove it from the node list
    randomNode = random.choice(eligibleNodes)
    eligibleNodes.remove(randomNode)
    
    # List of all nodes with their values, current one (randomNode) removed
    nodeValues = list(G.nodes(data=True))
    nodeValues.remove((randomNode,G.node[randomNode]))

    # At the begining we have a fully non-connected graph so we make an edge between two random node
    if i == 0 :
        
        nodeToConnect = random.choice(nodeValues)[0]
        G.add_edge(randomNode,nodeToConnect)
        
        G.node[randomNode]['realValue'] = 1
        
        G.node[nodeToConnect]['realValue'] = 1

    else :
        # Make a list of all nodes with the highest value
        maxValue = 0
        maxValueNode = None

        for node in nodeValues :
            nodeValue = node[1]['realValue']
            
            inferedNodeValue = (random.randrange(5,195)/100)*nodeValue

            if inferedNodeValue > maxValue :
                maxValue = inferedNodeValue
                maxValueNode = node[0]

                
        
        # Random choose of one of the higher value nodes
        nodeToConnect = maxValueNode
    
        # If there isn't already an edge between the two nodes
        if G.has_edge(nodeToConnect,randomNode) == False :
            
            # Connect the selected node (randomNode) with a node that will maximize his value
            G.add_edge(randomNode,nodeToConnect)
            
            if G.degree[randomNode] == 1 :
                G.node[randomNode]['realValue'] = 1
            
            if G.degree[nodeToConnect] == 1 :
                G.node[nodeToConnect]['realValue'] = 1

            if  G.degree[randomNode] > 1:
                nodeNeighbours = G[randomNode]
                G.node[randomNode]['realValue'] = 0
                for neighbourNode in nodeNeighbours :
                    G.node[randomNode]['realValue'] += G.node[neighbourNode]['realValue']
            
            if G.degree[nodeToConnect] > 1 :
                nodeNeighbours = G[nodeToConnect]
                G.node[nodeToConnect]['realValue'] = 0
                for neighbourNode in nodeNeighbours :
                    G.node[nodeToConnect]['realValue'] += G.node[neighbourNode]['realValue']

displayGraph(G)







