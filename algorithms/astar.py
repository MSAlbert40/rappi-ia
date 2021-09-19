import heapq
from math import sqrt


# Class Node complement with Algorithm
class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.f, self.g, self. h = 0, 0, 0

    @staticmethod
    def Euclidian(start, end):
        distance = sqrt((end.position[0] - start.position[0]) ** 2 + (end.position[1] - start.position[1]) ** 2)
        return distance

    @staticmethod
    def Manhattan(start, end):
        distance = abs(start.position[0] - end.position[0]) + abs(start.position[1] - end.position[1])
        return distance

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f


# Algorithm A-Star
class AStar:
    @staticmethod
    def solveAStar(mapPrincipal, start, target, heuristic):
        startNode = Node(None, start)
        targetNode = Node(None, target)
        opened = []
        closed = []
        evaluated = []

        n = len(mapPrincipal)
        heapq.heappush(opened, startNode)

        while len(opened) > 0:
            currentNode = heapq.heappop(opened)
            if currentNode == targetNode:
                path = []
                current = currentNode
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1], evaluated

            successors = []
            for movement in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                coordX = currentNode.position[0] + movement[0]
                coordY = currentNode.position[1] + movement[1]

                if coordX > n - 1 or coordX < 0 \
                        or coordY > (n - 1) or coordY < 0:
                    continue
                if mapPrincipal[coordX][coordY] != 1 and mapPrincipal[coordX][coordY] != 9 \
                        and mapPrincipal[coordX][coordY] != 11:
                    continue

                evaluated.append((coordX, coordY))
                newNode = Node(currentNode, (coordX, coordY))
                successors.append(newNode)

            for s in successors:
                for c in closed:
                    if s == c:
                        continue
                s.g = currentNode.g + 1
                s.h = heuristic(s, targetNode)
                s.f = s.g + s.h
                heapq.heappush(opened, s)