from time import time
from Iterative_deepening_DFS import run_IDDFS
from Bidirectional_search import run_Bidirectional
from Greedy import greedy
from Astar_search import Astar_search
from RBFS_search import recursive_best_first_search

'''
Assignment
1. Iterative deepening depth-first-search
2. Bidirectional search
3. Greedy best-first search
4. A* search
5. Recursive-Best-First-Search (RBFS)
'''

state=[

       [2, 8, 1,
        0, 4, 3,
        7, 6, 5],

       [0, 2, 1,
        4, 8, 6,
        7, 5, 3],

       [4, 2, 1,
        8, 3, 5,
        7, 6, 0],

        ]

goal_node = [4, 2, 1, 8, 0, 3, 7, 6, 5]

for i in range(len(state)):
    print("Start node",state[i])
    print()
    t0 = time()
    iddfs_instance = run_IDDFS(state[i])
    print('IDDFS:',iddfs_instance[0])
    t1 = time() - t0
    print('time:', iddfs_instance[1]*1000)
    print()

    t0 = time()
    bidirectional_instance = run_Bidirectional(state[i], goal_node)
    print('Bidirectional:',bidirectional_instance[1])
    t1 = time() - t0
    print('time:', t1*1000)
    print()

    t0 = time()
    greedy_result = greedy(state[i], goal_node)
    t1 = time() - t0
    print('Greedy:',greedy_result)
    print('time:', t1*1000)
    print()

    t0 = time()
    astar = Astar_search(state[i])
    t1 = time() - t0
    print('A*:',astar)
    print('time:', t1*1000)
    print()

    t0 = time()
    RBFS = recursive_best_first_search(state[i])
    t1 = time() - t0
    print('RBFS:',RBFS)
    print('time:', t1*1000)

    print('-------------------------------------------------------------------------------')
    print('-------------------------------------------------------------------------------')