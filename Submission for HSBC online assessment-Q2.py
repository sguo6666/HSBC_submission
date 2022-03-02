#!/usr/bin/env python
# coding: utf-8


# Question 2:




def minPossLen(posK, retailerXCord, headXCord, headYCord):
    # define function for the distance
    def dist(x1,x2):
        distance = ((x1[0]-x2[0])**2 + (x1[1]-x2[1])**2) **0.5
        return distance
    
    # transform input to coordinates
    head_rtl = [x_N1, y_N1]
    rtls = [[i,0] for i in x_N]
    start = [K,0]
    
    # construct a graph of connections among retailers
    graph = {}
    graph['start'] = {}
    for i in range(N):
        graph['start']["x_"+str(i+1)] = dist(start,rtls[i])
    graph['start']['head'] = dist(start,head_rtl)

    graph["head"] = {}
    for j in range(N):
        graph["x_"+str(j+1)] = {}
        for k in range(N):
            if k != j:
                graph["x_"+str(j+1)]["x_"+str(k+1)] = dist(rtls[j],rtls[k])
            else: continue
        graph["x_"+str(j+1)]["head"] = dist(rtls[j],head_rtl)
        graph["head"]["x_"+str(j+1)] = dist(head_rtl,rtls[j])
        
    # calculate the shortest distance to cover all retailers including head retailer, sequence does not matter
    path = {}
    dists = {}
    step = 0
    retailer = 'start'

    while step <= N:
        dist = sum(dists.values())
        step += 1
        neighbors = graph[retailer]

        shortest_dist = float("inf")
        path["Step"+str(step)] = ['placeholder',shortest_dist]
        for r in neighbors.keys():
            if r not in list(dists.keys()):
                new_dist = dist + neighbors[r]
                if path["Step"+str(step)][1] > new_dist:
                    path["Step"+str(step)] = [r,new_dist]

        retailer,distance = path["Step"+str(step)]
        dists[retailer] = distance  
    return distance

def main():
    posK = int(input())
    retailerXCord = []
    retailerXCord_size = int(input())
    retailerXCord = list(map(int,input().split()))

    headXCord = int(input())
    headYCord = int(input())
    
    result = minPossLen(posK, retailerXCord, headXCord, headYCord)
    print(result)
    
if __name__ == "__main__":
    main()

