from collections import deque
import heapq
import numpy as np
import random
import sys
 
N = 3
list_path= [ ]

class Node:
  dirs = [0, -1, 0, 1, 0]
  def __init__(self, state, parent = None, h = 0):
    self.state = state
    self.parent = parent
    self.g = parent.g + 1 if parent else 0
    self.h = h
    self.f = self.g + self.h
 
  def getMoves(self):
    moves = []
    index = self.state.index(0)
    x = index % N
    y = index // N
    for i in range(4):
      tx = x + Node.dirs[i]
      ty = y + Node.dirs[i + 1]
      if tx < 0 or ty < 0 or tx == N or ty == N:
        continue
      i = ty * N + tx
      move = list(self.state)
      move[index] = move[i]
      move[i] = 0
      moves.append(tuple(move))
    return moves
 
  def print(self):
    return list(np.reshape(self.state, -1))
 
  def __lt__(self, other):
    return self.f < other.f
 
def getRootNode(n):
  return getRootNode(n.parent) if n.parent else n
 
def BidirectionalBFS(start_state, end_state):
  def constructPath(p, o):
    while o: 
      t = o.parent
      o.parent = p
      p, o = o, t
    return p
  ns = Node(start_state)
  ne = Node(end_state)
  q = [deque([ns]), deque([ne])]
  opened = [{start_state : ns}, {end_state: ne}]
  closed = [0, 0]
  while q[0]:
    l = len(q[0])
    while l > 0:
      p = q[0].popleft()
      closed[0] += 1
      for move in p.getMoves():
        n = Node(move, p)
        if move in opened[1]:
          o = opened[1][move]
          if getRootNode(n).state == end_state:
            o, n = n, o
          n = constructPath(n, o.parent)
          return n, len(opened[0]) + len(opened[1]), closed[0] + closed[1]
        if move in opened[0]: continue
        opened[0][move] = n
        q[0].append(n)
      l -= 1
    q.reverse()
    opened.reverse()
    closed.reverse()
  return None, len(opened[0]) + len(opened[1]), closed[0] + closed[1]
 
def print_path(n):
  if not n: 
    return
  print_path(n.parent)
  global list_path
  # print(n.print())
  list_path.append(n.print())
  return list_path
  
def run_Bidirectional(start_node, goal_node):
  
    path, opened, closed = BidirectionalBFS(tuple(start_node), tuple(goal_node))
    # print(type(print_path(path)))
    
    return print_path(path), print_action(print_path(path))

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

# if __name__ == '__main__':
#     result = run_bidirectional()
#     print(print_action(result))