import collections
import queue
import time
import itertools

class Node:

    def __init__(self, puzzle, last=None):
        self.puzzle = puzzle
        self.last = last

    @property
    def seq(self): # to keep track of the sequence used to get to the goal
        node, seq = self, []
        while node:
            seq.append(node)
            node = node.last
        yield from reversed(seq)

    @property
    def state(self):
        return str(self.puzzle.board) # hashable so it can be compared in sets

    @property
    def isSolved(self):
        return self.puzzle.isSolved

    @property
    def getMoves(self):
        return self.puzzle.getMoves

class Puzzle:

    def __init__(self, startBoard):
        self.board = startBoard

    @property
    def getMoves(self):

        possibleNewBoards = []

        zeroPos = self.board.index(0) # find the zero tile to determine possible moves

        if zeroPos == 0:
            possibleNewBoards.append(self.move(0,1))
            possibleNewBoards.append(self.move(0,3))
        elif zeroPos == 1:
            possibleNewBoards.append(self.move(1,0))
            possibleNewBoards.append(self.move(1,2))
            possibleNewBoards.append(self.move(1,4))
        elif zeroPos == 2:
            possibleNewBoards.append(self.move(2,1))
            possibleNewBoards.append(self.move(2,5))
        elif zeroPos == 3:
            possibleNewBoards.append(self.move(3,0))
            possibleNewBoards.append(self.move(3,4))
            possibleNewBoards.append(self.move(3,6))
        elif zeroPos == 4:
            possibleNewBoards.append(self.move(4,1))
            possibleNewBoards.append(self.move(4,3))
            possibleNewBoards.append(self.move(4,5))
            possibleNewBoards.append(self.move(4,7))
        elif zeroPos == 5:
            possibleNewBoards.append(self.move(5,2))
            possibleNewBoards.append(self.move(5,4))
            possibleNewBoards.append(self.move(5,8))
        elif zeroPos == 6:
            possibleNewBoards.append(self.move(6,3))
            possibleNewBoards.append(self.move(6,7))
        elif zeroPos == 7:
            possibleNewBoards.append(self.move(7,4))
            possibleNewBoards.append(self.move(7,6))
            possibleNewBoards.append(self.move(7,8))
        else:
            possibleNewBoards.append(self.move(8,5))
            possibleNewBoards.append(self.move(8,7))

        return possibleNewBoards # returns Puzzle objects (maximum of 4 at a time)

    def move(self, current, to):

        changeBoard = self.board[:] # create a copy
        changeBoard[to], changeBoard[current] = changeBoard[current], changeBoard[to] # switch the tiles at the passed positions
        return Puzzle(changeBoard) # return a new Puzzle object

    def printPuzzle(self): # prints board in 8 puzzle style

        copyBoard = self.board[:]
        
        return copyBoard


    @property
    def isSolved(self):
        return self.board == [4, 2, 1, 8, 0, 3, 7, 6, 5]

class Solver:

    def __init__(self, Puzzle):
        self.puzzle = Puzzle

    def IDDFS(self):

        def DLS(currentNode, depth):
            if depth == 0:
                return None
            if currentNode.isSolved:
                return currentNode
            elif depth > 0:
                for board in currentNode.getMoves:
                    nextNode = Node(board, currentNode)
                    if nextNode.state not in visited:
                        visited.add(nextNode.state)
                        goalNode = DLS(nextNode, depth - 1)
                        if goalNode != None: # I thought this should be redundant but it never finds a soln if I take it out
                            if goalNode.isSolved: # same as above ^
                                return goalNode

        for depth in itertools.count():
            visited = set()
            startNode = Node(self.puzzle)
            # print(startNode.isSolved)
            goalNode = DLS(startNode, depth)
            if goalNode != None:
                if goalNode.isSolved:
                    return goalNode.seq


def print_action(list_puzzle):
    list_temp_path_index = [ ] 
    for path in list_puzzle:
        x = path.index(0)
        i = int(x / 3)
        j = int(x % 3)
        list_temp_path_index.append((i,j))

    list_path = []
    for current_idx in range(1, len(list_temp_path_index)):
        previous_idx = current_idx-1
        row_prev = list_temp_path_index[previous_idx][0]
        column_prev = list_temp_path_index[previous_idx][1]
        row_current = list_temp_path_index[current_idx][0]
        column_current = list_temp_path_index[current_idx][1]
        if row_prev - row_current == 1:
            list_path.append("Up")
        elif column_prev - column_current == -1:
            list_path.append("Right")
        elif row_prev - row_current == -1:
            list_path.append("Down")
        elif column_prev - column_current == 1:
            list_path.append("Left")
    return list_path


def run_IDDFS(start_node):
    myPuzzle = Puzzle(start_node)
    mySolver = Solver(myPuzzle)
    start = time.time()
    goalSeq = mySolver.IDDFS()
    end = time.time()

    counter = -1
    list_temp = []
    for node in goalSeq:
        counter = counter + 1
        node.puzzle.printPuzzle()
        list_temp.append(node.puzzle.printPuzzle())
    totalTime = end - start
    return print_action(list_temp), totalTime