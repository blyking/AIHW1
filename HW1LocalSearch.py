import HW1NodeLocalSearch
import random

def printState():  #prints relevant information about the state of the search
    for key in nodes:
        print(f'Node: {nodes[key].getName()}')
        print(f'{nodes[key].getName()} color {nodes[key].getColor()}')
        print(f'{nodes[key].getName()} cant be colored  with {nodes[key].getCannotColor().keys()}')
        print(f'{nodes[key].getName()} can be colored with {nodes[key].getCanColor()}' )
    print('\n' + '\n' + '\n')

def findProblem():  #finds errors in the random coloring. Returns the first node that errors
    for key in nodes:
        if getConflictNumber(nodes[key]) > 0:
            return nodes[key]
    return None

def updateCannotColor(node):
    node.resetCannotColor()
    for key in node.getNeighbors():
        node.addToCannotColor(node.getNeighbors()[key].getColor())

def updateCanColor(node):
    node.resetCanColor()
    for key in colors:
        if not key in node.getCannotColor().keys():
            node.addToCanColor(colors[key])


def getConflictNumber(node):
    startNum = 0
    for key in node.getNeighbors():  #loop finds the total number of conflicts. Stores in startNum
        if node.getColor() == node.getNeighbors()[key].getColor():
            startNum = startNum + 1
    return startNum

def changeBestColor(node):  #changes the color of the node, such that the total number of conflicts around the node is minimized.
    startNum = getConflictNumber(node)  #starting number of conflicts for the problem node
    if startNum == 0:
        if len(list(node.getCanColor())) > 1:
            for key in node.getCanColor():
                if node.getCanColor()[key] != node.getColor():
                    node.setColor(node.getCanColor()[key])
                    for key in node.getNeighbors():  # add node to neighbors cannot color list
                        updateCannotColor(node.getNeighbors()[key])
                        updateCanColor(node.getNeighbors()[key])
                break
        updateCanColor(node)
        updateCannotColor(node)
        return
    newNum = startNum
    i = 0
    while(startNum <= newNum): #if num new conflicts less, then return. If we have checked every color without reducing, also return
        #printState()
        if i > len(list(node.getCanColor())):
            newNode = node.getNeighbors()[list(node.getNeighbors().keys())[int(random.uniform(0, len(list(node.getNeighbors().keys()))))]]  # jump to one of the nodes neighbors
            changeBestColor(newNode)  # try to color this node to reduce conflicts
            updateCannotColor(node)
            updateCanColor(node)
            return
        if len(list(node.getCanColor().keys())) > 0:  #if there are possible colors, color the node one of them, then check conflicts
            newColor = node.getCanColor()[list(node.getCanColor().keys())[int(random.uniform(0, len(node.getCanColor().keys())))]]
            oldColor = node.getColor()
            node.setColor(newColor)  #set color

            for key in node.getNeighbors():  #add node to neighbors cannot color list
                updateCannotColor(node.getNeighbors()[key])
                updateCanColor(node.getNeighbors()[key])

            updateCannotColor(node)
            updateCanColor(node)

            newNum = getConflictNumber(node)  #recalculate number of conflicts.
            i = i + 1
        elif(len(list(node.getCannotColor().keys())) == len(colorsList)):  #if the conflict node is totally "locked", then we cannot color it such that the number of conflicts will be reduced, so jump
            newNode = node.getNeighbors()[list(node.getNeighbors().keys())[int(random.uniform(0, len(list(node.getNeighbors().keys()))))]]  #jump to one of the nodes neighbors
            print(newNode.getName())
            changeBestColor(newNode)  #try to color this node to reduce conflicts
            updateCannotColor(node)
            updateCanColor(node)
            return
    return

def localSearch():
    node = findProblem()  #see if there is problem in the graph. If there isnt, return
    while(node != None):  #if there is problem, try to fix it
        print(node.getName())
        updateCannotColor(node)
        changeBestColor(node)
        node = findProblem()  #if there are now no problems, the function will return
    return

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
        #nodes[entry].setColor(colorsList[0])
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

for key in nodes:  #for each node get the nodes neighbors, get
    for key1 in colors:
        if key1 not in nodes[key].getCannotColor():
            nodes[key].addToCanColor(colors[key1])

node = None
for keys in nodes:
    if len(nodes[keys].getNeighbors()) == 0: continue
    node = nodes[keys]

print(len(nextNode.getCannotColor()))

printState()
localSearch()
printState()