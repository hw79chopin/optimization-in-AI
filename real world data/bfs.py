import time
from queue import Queue, PriorityQueue
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

def Breadth_First_Search(graph, start, end, df, df_long_lat):
    frontier = Queue()
    frontier.put(start)
    explored = []

    print("\n========================================")
    print("BFS")
    start_station_name = df[df['from_station_ID']==int(start)].iloc[0]['from']
    end_station_name = df[df['from_station_ID']==int(end)].iloc[0]['from']
    print("Start: {} ({}), Goal: {} ({})".format(start, start_station_name,  end, end_station_name))

    count = 0
    distance = 0
    while True:
        if frontier.empty():
            raise Exception("No way Exception")
        current_node = frontier.get()
        if len(explored) != 0:
            previous_node = explored[-1]
            distance += haversine(df_long_lat[df_long_lat['NODE_ID']==int(previous_node)].iloc[0]['longitude'],
                                  df_long_lat[df_long_lat['NODE_ID']==int(previous_node)].iloc[0]['latitude'],
                                  df_long_lat[df_long_lat['NODE_ID']==int(current_node)].iloc[0]['longitude'],
                                  df_long_lat[df_long_lat['NODE_ID']==int(current_node)].iloc[0]['latitude'])*1000
        explored.append(current_node)
        count += 1
        try:
            station_name = df[df['from_station_ID']==int(current_node)].iloc[0]['from']
        except: 
            station_name = df[df['to_station_ID']==int(current_node)].iloc[0]['from']
        print("{}th loop".format(count) , "| visited node: {} ({})".format(current_node,station_name ))

        # Check if node is goal-node
        if current_node == end:
            print("Total distance: {}km".format(round((distance / 1000), 3)))
            return

        for node in graph[current_node]:
            if node not in explored:
                frontier.put(node)