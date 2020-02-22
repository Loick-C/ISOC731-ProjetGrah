# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 14:10:49 2020

@author: Tanguy
"""

import networkx as nx
import random
import matplotlib.pyplot as plt

def displayGraph(graph, figureName) :
    plt.figure(figureName)
    nx.draw(graph,with_labels=True, font_weight='bold')

def buildGraph(nodeNumber) :
    n = nodeNumber # Number of nodes
    
    # Building graph with n non-connected nodes
    G = nx.Graph()
    for i in range(1,n+1) :
        G.add_node(i,realValue=0,karma=0,defect=0,defectOrNot=0)
    
    eligibleNodes = list(G.nodes)
    
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

    return G

graph = buildGraph(100)
displayGraph(graph, "Graphe initiale")

allNodes = list(graph.nodes)
godNodeValues = []
godNodeDegrees = []
clusterSizes=[]
for i in range(0,500) :
    
    if allNodes == [] :
        allNodes = list(graph.nodes)
    
    currentNode = random.choice(allNodes)
    allNodes.remove(currentNode)

    
    nodeNeighbours = graph[currentNode]
    nodesToBreakEdge = []
    for neighbourNode in nodeNeighbours :
        
        graph.node[currentNode]['defectOrNot'] += 1
        randomValue = random.random()
        if randomValue >= 0.5 :
            nodesToBreakEdge.append(neighbourNode)
            
    for nodeToBreakEdge in nodesToBreakEdge :
        graph.node[currentNode]['defect'] += 1
        graph.remove_edge(currentNode,nodeToBreakEdge)
        
    if graph.node[currentNode]['defectOrNot'] > 0 :
        graph.node[currentNode]['karma'] = graph.node[currentNode]['defect'] / graph.node[currentNode]['defectOrNot']
    
    nodesToConnect = list(graph.nodes(data=True))
    nodesToConnect.remove((currentNode,graph.node[currentNode]))
    nodesToConnect = [item for item in nodesToConnect if item not in nodesToBreakEdge]
    
    lowerKarmaValue = min(nodesToConnect,key=lambda item:item[1]['karma'])[1]['karma']
    minKarmaNodes = []
    for nodeToConnect in nodesToConnect :
        if nodeToConnect[1]['karma'] == lowerKarmaValue :
            minKarmaNodes.append(nodeToConnect[0])
    
    lowerKarmaNode = random.choice(minKarmaNodes)     
    if graph.has_edge(currentNode,lowerKarmaNode) == False :
        graph.add_edge(currentNode,lowerKarmaNode)
    
    if graph.degree[currentNode] == 1 :
        graph.node[currentNode]['realValue'] = 1
        
    if graph.degree[currentNode] == 0 :
        graph.node[currentNode]['realValue'] = 0
                
    if graph.degree[lowerKarmaNode] == 1 :
        graph.node[lowerKarmaNode]['realValue'] = 1
        
    if graph.degree[lowerKarmaNode] == 0 :
        graph.node[lowerKarmaNode]['realValue'] = 0
    
    if  graph.degree[currentNode] > 1:
        nodeNeighbours = graph[currentNode]
        graph.node[currentNode]['realValue'] = 0
        for neighbourNode in nodeNeighbours :
            graph.node[currentNode]['realValue'] += graph.node[neighbourNode]['realValue']
            
    if graph.degree[lowerKarmaNode] > 1 :
        nodeNeighbours = graph[lowerKarmaNode]
        graph.node[lowerKarmaNode]['realValue'] = 0
        for neighbourNode in nodeNeighbours :
            graph.node[lowerKarmaNode]['realValue'] += graph.node[neighbourNode]['realValue']
    
    godNodeValues.append(graph.node[50]['realValue'])
    godNodeDegrees.append(graph.degree[50])
    clusterSizes.append(len(max(nx.connected_component_subgraphs(graph), key=len))/100)

displayGraph(graph,"Graphe après")
print(graph.degree)
plt.figure('Size')
plt.plot(clusterSizes)
plt.figure('God Node')
plt.plot(godNodeValues)
plt.figure('Degree')
plt.plot(godNodeDegrees)








