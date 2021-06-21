#! /usr/bin/env python
# coding: utf-8


path_matrix = {
    'A': {'B': 4, 'C': 6, 'D': 6, 'E': float("inf"), 'F': float("inf"), "G": float("inf")},
    'B': {'A': float("inf"), "C": 1, "D": float("inf"), "E": 7, "F": float("inf"), "G": float("inf")},
    'C':{'A':float("inf"),'B':float("inf"),'D':float("inf"),'E':6,'F':4,'G':float("inf")},
    'D':{'A':float("inf"),'B':float("inf"),'C':2,'E':6,'F':4,'G':float("inf")},
    'E':{'A':float("inf"),'B':float("inf"),'C':float("inf"),'D' :float("inf"),'F':float("inf"),'G':6},
    'F':{'A':float("inf"),'B':float("inf"),'C':float("inf"),'D' :float("inf"),'E':1,'G':8},
    'G':{'A':float("inf"),'B':float("inf"),'C':float("inf"),'D' :float("inf"),'E':1,'F':float("inf")}
}

def get_shortest_path(path_maxtrix,origin_node):
    '''
    根据dijkstra算法求解从origin_node出发到各点的路径
    :param path_maxtrix: 各点到各点的路径情况，dict类型
    :param origin_node: 起始位置，str类型
    :return: origin_node到各点的最短距离，dict类型
    '''
    visited_node = [origin_node]
    result=path_maxtrix[origin_node]
    del path_maxtrix["A"]
    unvisited_list = list(path_maxtrix.keys())
    # print(visited_node)
    # print(unvisited_list)
    # print(result)
    # print(path_matrix)

    while len(unvisited_list):
        temp_node = visited_node[-1]
        if temp_node!=origin_node: # 如果不是起始点
            distance_list=[]
            node_list=[]
            for item in unvisited_list:
                distance_list.append(path_matrix[temp_node][item])
                node_list.append(item)
                print(result[temp_node]+path_matrix[temp_node][item])
                if result[item]>result[temp_node]+path_matrix[temp_node][item]:
                    result[item]=result[temp_node]+path_matrix[temp_node][item]

            min_dist=min(distance_list)
            the_index=distance_list.index(min_dist)
            min_node=unvisited_list.pop(the_index)
            visited_node.append(min_node)

        else: # 如果是起始点
            # 找到距离起点路径最短的地点
            min_key = list(result.keys())[0]
            min_path=result[min_key]
            for key,value in result.items():
                if value<min_path:
                    min_path=value
                    min_key=key

            visited_node.append(min_key)
            the_index=unvisited_list.index(min_key)
            unvisited_list.pop(the_index)

    print(result)

get_shortest_path(path_matrix,"A")