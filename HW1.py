import HW1Node

#local location of input, need to change so it reads from command line
data = open('C:\\Users\\ppsmith\\Desktop\\AustraliaColoring.txt', 'r')

#open and read the data
data = data.readlines()

#colors will contain the colors provided, nodes will be a list of nodes provided
colors = {}
nodes = {}

set = 0

#for each line the data, do the following. This the parser. The parser produces a list of colors, dictionary of nodes, and intializes the properties of each node.
#set counts the number of black lines that we haves seen. Creates seperation between the input parts.
for entry in data:
    if entry != '\n' and set == 0:
        entry = entry.strip('\n')
        colors[entry] = entry;
        continue
    elif entry == '\n' and set == 0:  # if we encounter blank line, we know we are done with the colors and can move on to the nodes.
        set = 1
        continue

    if entry != '\n' and set == 1:
        entry = entry.strip('\n')
        nodes[entry] = HW1Node.Node(entry)  #creates a new node in the nodes dictionary and intializes that nodes name. The key in the dictionart is the name of the node
        continue
    elif entry == '\n' and set == 1:
        set = 2;
        continue

    if entry != '\n' and set == 2:
        if (entry == '\n'): continue
        entry = entry.strip('\n')
        entry = entry.split()
        tmpNode = entry[0]
        tmpoNode2 = entry[1]
        node0 = nodes[tmpNode]
        node1 = nodes[tmpoNode2]
        node0.addNeighbors(node1)

root = nodes[next(iter(nodes))]

while not root.hasNeightbors():
    root = nodes[next(iter(nodes))]
    root.setColor(colors[1])
tmp = root

maxCount = 0
maxKey = ''
for key in nodes:
    neighbors = len(nodes[key].getNeighbors())
    if neighbors > maxCount:
        maxCount = neighbors
        maxKey = key

root = nodes[maxKey]
previous = []
newColor = ''

print('Max root: ' + root.getName())

tmp = root  #tmp is a node
tmp.setColor(colors[next(iter(colors))])
tmp.setColored(1)
tmp.addToCannotColor(tmp.getColor())
tmp.setSeen(1)
for key in tmp.getNeighbors():
    tmp.getNeighbors()[key].addToCannotColor(tmp.getColor())


while tmp.hasUnexploredNeighbors():  #while the node has neighbors that have not been seen
    try:
        previous.append(tmp)  #append the node to the list of previous nodes
        key = iter(tmp.getNeighbors())  #create an iterable over the keys
        tmp = nodes[next(key)]  #new node is the first node in the neightbors list

        colorTestIter = iter(colors)  #create an iterator over the colors dict.
        testColor = tmp.getCannotColor()  #get dict. of uincolorable colors
        i = 0
        while i < len(colors.keys()):  #while there are colors to look at
            nextKey = next(colorTestIter)
            i = i + 1
            if not nextKey in testColor:
                tmp.setColor(colors[nextKey])
                tmp.addToCannotColor(tmp.getColor())
                tmp.setColored(1)
                for key in tmp.getNeighbors():
                    tmp.getNeighbors()[key].addToCannotColor(tmp.getColor())
                continue
            continue
        tmp = previous.pop()
        continue
    except:
        for key in nodes:
            print('Name: ' + nodes[key].getName())
            print(nodes[key].getColor())
            print('\n')













