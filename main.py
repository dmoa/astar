def addPositions(pos1, pos2):
    return (pos1[0] + pos2[0], pos1[1] + pos2[1])

# manhattan method, instead of using abs() we just square it
def getDistance(node1, node2):
    return (node1[0] - node2[0])**2 + (node1[1] - node2[1])**2

class Node():
    def __init__(self, parent=None, position=None, g = 0, h = 0, cost = 0):
        self.parent = parent
        self.position = position
        self.g = g
        self.h = h
        self.cost = cost


def astar(maze, start, end):

    start_node = Node(None, start)
    end_node = Node(None, end)

    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # getting the node in open list which has the least cost
    while len(open_list) > 0:

        minCostIndex = 0
        tempCost = open_list[0].cost
        for index, node in enumerate(open_list):
            if node.cost < tempCost:
                minCostIndex = index
                tempCost = node.cost

        # switch lowest cost square from open list to closed list
        closed_list.append(open_list.pop(minCostIndex))
        currentNode = closed_list[-1]

        if currentNode.position == end_node.position:
            print("solution found!")
            #  cycling pack through parents to get the path
            path = []
            IterativeNode = currentNode
            # while the node still has a parent node, keep getting all those parent nodes!
            while IterativeNode.parent != None:
                path.append(IterativeNode.position)
                IterativeNode = IterativeNode.parent
            path.append(start_node.position)

            return path[::-1]
        else:
            print("solution not found")

        # 4 adjacent squares around the node
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            newNodePos = addPositions(currentNode.position, direction)

            # if it is out of bounds, skip iteration and move onto next surrounding square
            if newNodePos[0] > len(maze) - 1 or newNodePos[0] < 0 or newNodePos[1] > len(maze[0]) - 1 or newNodePos[1] < 0:
                continue

            # if it is in closed list, skip iteration
            # this is to avoid infinite loops
            if Node(currentNode, newNodePos) in closed_list:
                continue

            # if position is an obstacle, skip iteration
            # this is because the path cannot go through walls

            if maze[newNodePos[1]][newNodePos[0]] == 1:
                continue

            # check if the new node we just calculated is already in open_list
            InOpenList = False
            # this variable we only use if InOpenList is false, i.e. if it's in open list
            # we use it to check whether we have the minimum g value possible
            # it saves us time from having to find the duplicate item again
            repeatedNodeIndex = 0
            for index, node in enumerate(open_list):
                if node.position == newNodePos:
                    InOpenList = True
                    repeatedNodeIndex = index
                    break

            # if the new node isn't on the open_list, add it
            if not InOpenList:
                g = currentNode.g + 1
                h = getDistance(end_node.position, newNodePos)
                cost = g + h
                open_list.append(Node(currentNode, newNodePos, g, h, cost))
            else:
                if currentNode.g < open_list[repeatedNodeIndex].g:
                    open_list[repeatedNodeIndex].parent = currentNode
                    open_list[repeatedNodeIndex].g = currentNode.g + 1


def main():

    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (5, 1)

    path = astar(maze, start, end)
    # print(maze)
    # print()
    print(path)


main()