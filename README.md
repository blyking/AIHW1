# AIHW1
HWAI
Project: COMP560 Assignment 1

Authors:
Blythe King
Phillip Smith

Note: Only Dr. Palay was added to the repository because only 3 collaborators can be added to a private repository on a free personal GitHub account.

***Coded in Python with PyCharm

Description:
The contents of this GitHub provide a backtracking search method and a local search method for coloring in a map. As the names suggest, the "HW1Backtrack.py" file provides the solution for the backtracking search (based off of the most constrained node) method, and the "HW1LocalSearch.py" file provides the solution for the local search (based off of hill climbing) method. The node classes are different. Please download them both. 

How to Run:
These files can be downloaded and run in PyCharm or another Python file editor (such as Jupyter Notebook or Visual Studio Code), which is likely the most straightforward way to run this program. Otherwise, a command-line interface can be used, such as the command prompt for Windows. To run, navigate to the file location using cd (in one user's case, this path is C:\Users\blyki\PycharmProjects\COMP560_A1 but will differ computer to computer) and then type python HW1Backtrack.py for to run the backtracking method and python HW1LocalSearch.py to run the local search method. From there, you will be prompted to enter a file path for the text file you wish to input. If using the USA map, an example of what could be inputted would be C://Users//blyki//OneDrive//Documents//UNC//Senior//COMP560//Assignments//A1//USA_Map.txt. Again, this path will differ computer to computer, as this program was designed under the assumption the user would already have the map text file downloaded. Afterwards, the solution
will be printed, with the node name, color, and additional information printed in the terminal.

Backtracking Method Overview:
1) List of colors to use are read in from text file.
2) Nodes are read in as classes with their names, neighbors, and colors. All nodes start off as "uncolored" (labeled "black" in our code).
3) While the length of black/uncolored nodes is greater than 0 (meaning there is an uncolored node), the backtracking function will run.
4) The initial node to start with is the most constrained node (the node with the most neighbors).
5) If a node has not been colored, and none of its neighbors are colored/does not have neighbors, then it's colored the first color in the color set read from the text file.
6)  If a node has not been colored, but one or more of its neighbors have been colored, the colors of the neighbors are added to that node’s “cannot be colored” list. The node is colored with the first/whatever remaining viable color is left in the color list that does not overlap with the “cannot be colored” list.
7) If a node is reached that has been colored, but has no uncolored neighbors, the code will backtrack back until it hits a node with uncolored neighbors, or the root node. 
8) If a node is reached, and the node cannot be colored because of the colors of its neighbors, the code will backtrack and attempt to change the color of the previous node. If the node one layer back cannot have its color changed, then we back up further until a color change can be made. Once that change is made, it is propagated back down. 
8) When a node has been successfully colored, it is added to the “previous” stack, and it next attempts to color the most constrained neighbor.
9) When this program is done running, a list of nodes and corresponding colors is printed.

Local Search Method Overview:
1) Nodes are read in from a text file in the same way as in the backtrack method. There are additional methods though. The node now keeps track of its cannotColor list (same as backtrack), as well as canColor list, which is the opposite of the cannotColor list. These two lists are used to check for contradictions, as well as to determine which colors a node can be. 
2) During the local search, all nodes are assigned random colors before being colored according to the local search method.
3) The program first identifies if there is a “problem” in the graph, meaning if two neighbors are the same color. If no problems are identified, then the program returns.
4) Otherwise, the code attempts to fix it. The program finds the “problem node” and identifies the color it should be in order to reduce the number of problems (contradictions). The node is always colored, but if the random color selected does not reduce the number of conflicts on the node, that color is not selected. Our heuristic is minimizing the number of conflicts on the node being worked on. When a node is colored, the values of the cannotColor and canColor lists of the node neighbors are updated.
5) If a node is encountered and there are no colors that can be used to reduce the number of conflicts, the code will shift to another, random neighbor of the starting node. The code will do this recursively until a node is found where the contradictions can be reduced. As the code pops back up, it updates the cannotColor and canColor lists. This is because when we run the code again, the problem nodes will still exist, but will not have fewer constraints on them (due to the minimization heuristic). 
6) The program checks again for any problems. If there are none, it returns and prints a list of nodes and their colors. Otherwise, step 5 is repeated until no problems are identified.
7) When this program is done running, a list of nodes and corresponding colors is printed.

Comments/Issues with Current Code Version:
1) For the backtrack method, finding the most constrained neighbor for each coloration adds extra steps to finding the solution rather than just starting at the most constrained node and then going to whatever the “first” neighbor in its neighbor list is.

2) Local search works around 60% of the time, and the state that causes the problem is known. If there is a situation a node’s contradictions cannot be minimized, and its neighbors have no contradictions, the code will run forever. This is because in order to break the deadlock, we would have to color one of the neighbors such that the contradictions on the neighbor node would increase. This is an example of a situation in which the “jump” solution to hill climbing does not work, because no matter where you jump, you will not be able to minimize any contradictions because all other contradictions are zero. Local minimum. 
