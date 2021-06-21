from sys import argv
from heapq import heappush, heappop

def Uniform_Search_Tree(graph, s, goal, df):
	# define dummy variables for use
	nodesQ = []
	visited_nodes = {}
	prev_nodes = {}
    
	start_station_name = df[df['from_station_ID']==int(s)].iloc[0]['from']
	goal_station_name = df[df['from_station_ID']==int(goal)].iloc[0]['from']
	print("Start: {} ({}), Goal: {} ({})".format(s, start_station_name,  goal, goal_station_name))

	# using heap for mainitng a queue
	heappush(nodesQ,(0,s,None,0))
	for nodes in graph:
		visited_nodes[nodes] = False
		prev_nodes[nodes] = None
	i = 0
	# mark all visited and previous nodes False and None
	while len(nodesQ) != 0:
		# pop the least cost node from heap and analyse it
		i = i+1
		total_cost, current_node, prev_node, link_cost = heappop(nodesQ)
		try:
			station_name = df[df['from_station_ID']==int(current_node)].iloc[0]['from']
		except: 
			station_name = df[df['to_station_ID']==int(current_node)].iloc[0]['from']
		print("{}th loop".format(i) , "| visited node: {} ({})".format(current_node, station_name))
		if visited_nodes[current_node] == False:
			visited_nodes[current_node] = True
			prev_nodes[current_node] = []
			prev_nodes[current_node].append(prev_node)
			prev_nodes[current_node].append(link_cost)
			# if goal return the total route
			if current_node == goal:
				final = []
				while current_node != s:
					temp = []
					temp.append(current_node)
					for i in prev_nodes[current_node]:
						temp.append(i)
					final.append(temp)
					current_node = prev_nodes[current_node][0]
				final.reverse()
				# retrn total cost and final path
				print("Total distance: {}km".format(round((total_cost / 1000), 3)))
				print("Optimal route: ", final)
				return total_cost, final
			# else explore neighbours
			for neighbors, ncost in graph[current_node].items():
				if visited_nodes[neighbors] == False:
					this_link_cost = ncost
					new_cost = total_cost + ncost
					heappush(nodesQ, (new_cost, neighbors, current_node, ncost))
	# return none if no path found
	return None
	pass