#define a node for this program. A node has four attributes
#1. A name that is a string
#2 a dictionary of other nodes that it is neighbors with. The keys in the dictionary are the node names
#3: A color

#This allows for every node to be able to determine the name and color of everynode it is neghibors with

class Node:
    #constructor
    def __init__(self, name):
        self.name = name  #name of the node
        self.neighbors = {}  #list of children
        self.color = 'black'  #starting color of the node
        self.seen = 0  #if the node has been seen
        self.cannotColor = {}
        self.colored = 0
        self.prevColors = {}  #list of previous colors

    #adds the 'node' to this node's list of neighbors
    def addNeighbors(self, node):
        if not (node.getName() in self.neighbors):  #check to ensure neighbor not already on the list
            self.neighbors[node.getName()] = node  # add the node to the neighbors list
            node.addNeighbors(self)  # add this node to the other nodes neighbors list
        return

    def getPrevColors(self):
        return self.prevColors

    #returns the name of the node
    def getName(self):
        return self.name

    def getSeen(self):
        return self.seen

    def setSeen(self, seen):
        self.seen = seen

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
            if self.neighbors[key].getColor() == 'black':
                count = count + 1
        return count

    def getFirstNonBlack(self):
        for key in self.neighbors:
            if self.neighbors[key].getColor() != 'black':
                return self.neighbors[key]

    def addToPrevColor(self, color):
        self.prevColors[color] = color

    def addToCannotColor(self, color):
        self.cannotColor[color] = color

    def removeFromCannotColor(self, color):
        for key in self.neighbors:
            garbage = self.neighbors[key].getCannotColor().pop(color)
        return

    def removeFromPreviousColor(self, color):
        self.prevColors.pop(color)

    def getCannotColor(self):
        return self.cannotColor

    def getColored(self):
        return self.colored

    def hasUnexploredNeighbors(self):
        for key in self.neighbors:
            if not self.neighbors[key].getColored():
                return 1
        return 0

    def getNextUnexplored(self):
        for key in self.neighbors:
            if 1 != self.neighbors[key].getColored():
                return self.neighbors[key]
        return 0

    def setColored(self, num):
        self.colored = num

    def getMostConstrainedNeighbor(self):
        max = 0
        maxNode = self
        for key in self.neighbors:
            if(len(self.neighbors[key].getNeighbors()) > max) and not self.neighbors[key].getColored():
                max = len(self.neighbors[key].getNeighbors())
                maxNode = self.neighbors[key]
        if maxNode == self:
            return None
        else:
            return maxNode


