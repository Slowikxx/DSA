# You are given a list of flight tickets where tickets[i] = [from_i, to_i] represents the source and destination airport
# Each from_i and to_i consists of three uppercase english letters
# Reconstruct the itinerary in order and return it

# All os the tickets belong to someone who originally departed from "JFK"
# Your objective is to reconstruct the flight path that this person took, assuming each ticket was used exactly once

from typing import List


def findItinerary(tickets: List[List[str]]) -> List[str]:
    adj = {src : [] for src, dst in tickets}
    tickets.sort()
    
    for src, dst in tickets:
        adj[src].append(dst)
    
    res = ["JFK"]
    
    def dfs(src):
        if len(res) == len(tickets) + 1:
            return True
        if src not in adj:
            return False
        
        
        temp = list(adj[src])
        for i, v in enumerate(temp):
            adj[src].pop(i)
            res.append(v)
            
            if dfs(v) : return True
            adj[src].insert(i,v)
            res.pop()
        return False
    
    dfs("JFK")
    return res

tickets1 = [["BUF", "HOU"], ["HOU", "SEA"], ["JFK", "BUF"]]
tickets2 = [["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]]

print(findItinerary(tickets1)) # Expected output: ["JFK","BUF","HOU","SEA"]
print(findItinerary(tickets2)) # Expected output: ["JFK","HOU","JFK","SEA","JFK"]

# Time complexity: O(e * v), where e is the number of tickets (edges) and v is the number of airports (vertices)
# Space complexity: O(e * v)