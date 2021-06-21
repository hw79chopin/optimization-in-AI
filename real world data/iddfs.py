# Global variables
# Contains string of visited states
visitedPaths = ""
# Contains final path from source to destination
finalPath = []
# Contains the total level of depth for each iteration
countOfDepth = 0
# Contains the source state
tempVar = ""
# number of loop
loop = 0

from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

def Iterative_Deepening_Depth_First_Search(source, destination, maxDepth, edges):
    '''
    Outer function to perform iterative deepening search.
    :param source: Starting state
    :param destination: Destination state
    :param maxDepth: Maximum number of depths that IDS can perform
    :param edges: List of edges in the map
    :return: List of final path
    '''
    global countOfDepth, visitedPaths, tempVar, loop
    tempVar = source

    # Check to perform if the source and destination is not in edges list
    if source not in edges.keys() or destination not in edges.keys():
        finalPath.append('FAIL')
        return finalPath

    
    for limit in range(maxDepth):
        # visited = source
        # print(source)
        countOfDepth = limit

        if depthLimitSearch(source, destination, limit, edges):
            # prints all the visited states
            print(visitedPaths, loop)
            finalPath.append(tempVar)
            finalPath.reverse()
            return finalPath
    # State not found. Hence, Fail.
    finalPath.append("FAIL")
    return finalPath


def depthLimitSearch(source, destination, limit, edges):
    '''
    Inner function that performs a depth limited search
    :param source: Current starting state from the edge list
    :param destination: Final destination state
    :param limit: Current depth to which DLS needs to be performed
    :param edges: List of edges in the map
    :return: Boolean True or False
    '''
    global countOfDepth, visitedPaths, tempVar, finalPath, loop
    loop += 1

    # Indents the visited states and appends the paths in visitedPaths
    if (countOfDepth-limit) <= 0:
        visitedPaths += '\n' + source
    else:
        visitedPaths += ('\n' + '\t' * (countOfDepth - limit)) + source

    # Checks if the the final destination has been reached
    if source == destination:
        return True

    # Checks whether all the depths have been traversed for the current iteration
    if limit < 1:
        return False

    # Temporary variable to remove the backward link from the edge-list data structure
    temp = []

    # Iterates over all connected states of a current state for a given depth
    for adjacentNode in edges[source]:
        # Removes the backward connection to visited nodes for eg.  connection between Arad - Zerind will remove Zering - Arad from the edges list
        temp = edges[adjacentNode]
        if source in temp:
            temp.remove(source)
            edges[adjacentNode] = temp
        #     Performs a recursive call to the DLS function with limit - 1
        if depthLimitSearch(adjacentNode, destination, limit - 1, edges):
            # Appends the final path once the destination state is reached
            finalPath.append(adjacentNode)
            return True
    return False

def get_distance(solution, df_node_lat_long):
    distance = 0
    for idx_1 in range(len(solution)-1):
        previous_node = solution[idx_1]
        current_node = solution[idx_1+1]
        distance += haversine(df_node_lat_long[df_node_lat_long['NODE_ID']==int(previous_node)].iloc[0]['longitude'],
                              df_node_lat_long[df_node_lat_long['NODE_ID']==int(previous_node)].iloc[0]['latitude'],
                              df_node_lat_long[df_node_lat_long['NODE_ID']==int(current_node)].iloc[0]['longitude'],
                              df_node_lat_long[df_node_lat_long['NODE_ID']==int(current_node)].iloc[0]['latitude'])*1000
    return str(round((distance/1000), 3)) + "km"