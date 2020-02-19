import HW1Node
import sys

def printState():  #prints relevant information about the state of the search
    for key in nodes:
        print(f'Node: {nodes[key].getName()}')
        print(f'{nodes[key].getName()} color {nodes[key].getColor()}')
        print(f'{nodes[key].getName()} cant be colored  with {nodes[key].getCannotColor().keys()}')
    print('\n' + '\n' + '\n')

def backTrack(tmp, steps):  #does a backtracking search. Starts with most constrsined nodes
    steps = steps + 1
    colorTestIter = iter(colors)  # create an iterator over the colors dict. keys
    while len(unColoredNodes) > 0:  #while there are nodes that need to be colored...
        #printState()
        #print(tmp.getName() + '\n')

        if tmp.getColored() and not tmp.hasUnexploredNeighbors():  #if the node has been colored, but has no neighbors, continue backing up
            if len(previous) == 0:  #enures that when backing up the recursion, a failure does not occure at the very end.
                return
            tmp = previous.pop()
            backTrack(tmp, steps)
            return
        elif tmp.getColored():  #if the node is colored, but has uncolored neighbors, backtrack on the uncolored neighbor
            for key in tmp.getNeighbors():
                if not tmp.getNeighbors()[key].getColored():
                    tmp = tmp.getNeighbors()[key]
                    break

        testColor = tmp.getCannotColor()  #get dict. of uncolorable colors  #get the colors the node cannot be colored
        i = 0  #keeps track of the colors tried

        #color the node
        while i < len(colors.keys()):  #while there are colors to look at...forward checking, will backup if
            nextKey = next(colorTestIter)  #next key is the next color key
            i = i + 1  #a color has been looked at...
            if not nextKey in testColor:  #if the color is not in nodes cannotColor list
                tmp.setColor(colors[nextKey])  #set the color
                tmp.setColored(1)  #set node to colored
                unColoredNodes.remove(tmp)  #remove node from list of uncolored nodes

                for keys in tmp.getNeighbors():  #loop adds color to neighbor's cannotColor lists
                    tmp.getNeighbors()[keys].addToCannotColor(tmp.getColor())


#//////////////////Code Between Slashes sets the next node to explore as the next most constrained node. This code added 13 steps to the solution, and so was taken out////////////////////////
                #test = tmp.getMostConstrainedNeighbor()

                #if test == None:
                    #tmp = previous.pop()
                    #backTrack(tmp, steps)
                    #return
                #else:
                    #previous.append(tmp)
                    #tmp = test
                    #backTrack(tmp, steps)
                    #return
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


                for keys in tmp.getNeighbors():  #if a the node has uncolored neighbors, switch the node to the uncolored node, and call backtrack
                    if tmp.getNeighbors()[keys].getColored() != 1:
                        previous.append(tmp)  #the placement of this line is important. If there is not an unseen neightbor, we do not want the current node to be in the previous list.
                                              #only add the node to previous once we have a node to move onto
                        tmp = tmp.getNeighbors()[keys]
                        backTrack(tmp, steps)
                        return
                tmp = previous.pop()  #if there is not a neighbor node that is not colored, back up and look for uncolored nodes in the previous node
                backTrack(tmp, steps)
                return
            continue

        #uncolor node because current config will not work
        tmp.removeFromCannotColor(tmp.getColor())  #removes the color from neighbors cannotColor lists
        tmp.setColor('black')  #reset color
        tmp.setColored(0)  #no longer colored
        tmp = previous.pop()  #backup and try again
        backTrack(tmp, steps)
        return
    print(f"Number of Steps: {steps}")
    return

#local location of input, need to change so it reads from command line
data = open(input('Please give file path'), 'r')

#open and read the data
data = data.readlines()
#colors will contain the colors provided, nodes will be a list of nodes provided
colors = {}  #used to hold possible colors
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
        continue
    elif entry == '\n' and set == 0:  # if we encounter blank line, we know we are done with the colors and can move on to the nodes.
        set = 1
        continue

    if entry != '\n' and set == 1:
        entry = entry.strip('\n')
        nodes[entry] = HW1Node.Node(entry)  #creates a new node in the nodes dictionary and initializes that nodes name. The key in the dictionary is the name of the node
        continue
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
    if(len(nodes[key].getNeighbors()) == 0):
        nodes[key].setColor(colors[next(iter(colors))])

maxCount = 0
maxKey = ''

#finds the most constrained node
for key in nodes:
    neighbors = len(nodes[key].getNeighbors())
    if neighbors > maxCount:
        maxCount = neighbors
        maxKey = key

root = nodes[maxKey]
previous = []
newColor = ''

tmp = root  #tmp is a node

#will show nodes and their neighbors
#for key in nodes:
#    print(f"{nodes[key].getName()}'s neighbors are {nodes[key].getNeighbors().keys()}")
#print('\n')

#add nodes to uncolored nodes list
for key in nodes:
    unColoredNodes.append(nodes[key])

#do backtracking search
backTrack(tmp, steps)

#print result
print("Print Backtracking Method Results:")
printState()
