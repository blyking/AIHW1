import HW1NodeLocalSearch
import random

def printState():  #prints relevant information about the state of the search
    for key in nodes:
        print(f'Node: {nodes[key].getName()}')
        print(f'{nodes[key].getName()} color {nodes[key].getColor()}')
        print(f'{nodes[key].getName()} cant be colored  with {nodes[key].getCannotColor().keys()}')
    print('\n' + '\n' + '\n')

def getHeuristc():
    maxLength = 0
    for key in nodes:
        if len(nodes[key].getCannotColor()) > maxLength:
            maxLength = len(nodes[key].getCannotColor())
            nextNode = nodes[key]
    return nextNode

def localSearch(node):
    nextNode = node.getNeighbors(next(iter(node.getNeighbors())))  #nextNode is the first neighbor
    nextNode.setColor(next(iter(can)))

#local location of input, need to change so it reads from command line
data = open(input('Please give file path'), 'r')

#open and read the data
data = data.readlines()
#colors will contain the colors provided, nodes will be a list of nodes provided
colors = {}  #used to hold possible colors
colorsList = []
nodes = {}  #used to hold nodes
unColoredNodes = []  #list of un-colored nodes
steps = 0  #total calls to backTrack()
set = 0  #used by parser

#for each line the data, do the following. This the parser. The parser produces a list of colors, dictionary of nodes, and intializes the properties of each node.
#set count the number of black lines that we haves seen. Creates seperation between the input parts.
for entry in data:
    if entry != '\n' and set == 0:
        entry = entry.strip('\n')
        colors[entry] = entry
        colorsList.append(entry)
        continue
    elif entry == '\n' and set == 0:  # if we encounter blank line, we know we are done with the colors and can move on to the nodes.
        set = 1
        continue

    if entry != '\n' and set == 1:
        entry = entry.strip('\n')
        nodes[entry] = HW1NodeLocalSearch.Node(entry)  #creates a new node in the nodes dictionary and initializes that nodes name. The key in the dictionary is the name of the node
        nodes[entry].setColor(colorsList[int(random.uniform(0, len(colors)))])  #sets nodes initial color to randomnodes

    elif entry == '\n' and set == 1:
        set = 2
        continue

    if entry != '\n' and set == 2:
        if (entry == '\n'): continue
        entry = entry.strip('\n')
        entry = entry.split()
        tmpNode = entry[0]
        tmpoNode2 = entry[1]
        node0 = nodes[tmpNode]
        node1 = nodes[tmpoNode2]
        node0.addNeighbors(node1)  #this method works on both nodes. For example WA SA will add WA to SA neighbors list, and add SA to WA neighbors list

for key in nodes:
    print(f"{nodes[key].getName()}'s neighbors are {nodes[key].getNeighbors().keys()}")
print('\n')

maxLength = 0

nextNode = HW1NodeLocalSearch.Node('test')

for key in nodes:  #want to add nodes color to cannot colors list of neighbors
    for neighbors in nodes[key].getNeighbors():
        nodes[key].getNeighbors()[neighbors].addToCannotColor(nodes[key].getColor())

node = getHeuristc()

print(len(nextNode.getCannotColor()))

localSearch(node)


printState()