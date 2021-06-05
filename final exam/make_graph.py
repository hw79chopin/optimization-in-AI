def make_graph_str(df_yonsei):
    dict_graph_str = {}

    for idx in df_yonsei.index:
        list_temp = []
        srcStation = str(df_yonsei.at[idx, 'from_station_ID'])
        destStation = str(df_yonsei.at[idx, 'to_station_ID'])

        if srcStation in dict_graph_str:
            dict_graph_str[srcStation] = dict_graph_str[srcStation] + [destStation]
        else:
            dict_graph_str[srcStation] = [destStation]

        if destStation in dict_graph_str:
            dict_graph_str[destStation] = dict_graph_str[destStation] + [srcStation]
        else:
            dict_graph_str[destStation] = [srcStation]
            
    return dict_graph_str

def make_graph_int(df_yonsei):
    dict_graph_int = {}

    for idx in df_yonsei.index:
        list_temp = []
        srcStation = df_yonsei.at[idx, 'from_station_ID']
        destStation = df_yonsei.at[idx, 'to_station_ID']

        if srcStation in dict_graph_int:
            dict_graph_int[srcStation] = dict_graph_int[srcStation] + [destStation]
        else:
            dict_graph_int[srcStation] = [destStation]

        if destStation in dict_graph_int:
            dict_graph_int[destStation] = dict_graph_int[destStation] + [srcStation]
        else:
            dict_graph_int[destStation] = [srcStation]
            
    return dict_graph_int

def make_graph_cost(df_yonsei):
    list_total = []
    for idx in df_yonsei.index:
        list_temp = []
        list_temp.append(df_yonsei.at[idx, 'from_station_ID'])
        list_temp.append(df_yonsei.at[idx, 'to_station_ID'])
        list_temp.append(df_yonsei.at[idx, 'distance(m)'])
        list_total.append(list_temp)

    dict_graph_cost = {}
    for rec in list_total:
        src = rec[0]
        dest = rec[1]
        cst = rec[2]
        if src not in dict_graph_cost:
            dict_graph_cost[src] = {}
        if dest not in dict_graph_cost:
            dict_graph_cost[dest] = {}
        # create src and dest nodes with its length from input file
        dict_graph_cost[src][dest] = float(cst)
        dict_graph_cost[dest][src] = float(cst)

    return dict_graph_cost

def make_graph_greedy(df_yonsei, df_node_lat_long):
    dict_graph_cost = make_graph_cost(df_yonsei)
    
    dict_map_maze = {}
    for key in dict_graph_cost.keys():
        list_adjacents = []
        for key_2 in dict_graph_cost[key]:
            tuple_adjacent = (str(key_2), dict_graph_cost[key][key_2])
            list_adjacents.append(tuple_adjacent)
        dict_map_maze[str(key)] = {'adjacent': list_adjacents, 
                                'point': (df_node_lat_long[df_node_lat_long['NODE_ID']==key].iloc[0]['longitude'],
                                            df_node_lat_long[df_node_lat_long['NODE_ID']==key].iloc[0]['latitude'])}
    return dict_map_maze