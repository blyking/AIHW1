#define a node for this program. A node has four attributes
#1. A name that is a string
#2 a dictionary of other nodes that it is neighbors with. The keys in the dictionary are the node names
#3: A color

#This allows for every node to be able to determine the name and color of everynode it is neghibors with

class Node:
    #constructor
    def __init__(self, name):
        self.name = name;
        self.neighbors = {}
        self.color = 'black'

    #adds the 'node' to this node's list of neighbors
    def addNeighbors(self, node):
        if not (node.getName() in self.neighbors):  #check to ensure neighbor not already on the list
            self.neighbors[node.getName()] = node  # add the node to the neighbors list
            node.addNeighbors(self)  # add this node to the other nodes neighbors list

    #returns the name of the node
    def getName(self):
        return self.name

    #set the color of the node
    def setColor(self, color):
        self.color = color

    #get color
    def getColor(self):
        return self.color

    #returns the dictionary of neighbors
    def getNeighbors(self):
        return self.neighbors

    def hasNeightbors(self):
        if(len(self.neighbors)) > 0:
            return 1
        else:
            return 0

    def numberBlack(self):
        count = 0
        for key in self.neighbors:
            if neighbors[key].getColor() == 'black':
                count = count + 1
        return count

    def getFirstNonBlack(self):
        for key in self.neighbors:
            if nodes[key].getColor() != 'black':
                return nodes[key];







