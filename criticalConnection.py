"""
TC: O(V+E) 
SP:O(V)
"""
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # create adj list
        adj_list = defaultdict(list)
        for u, v in connections:
            adj_list[u].append(v)
            adj_list[v].append(u)
        #create discovery and low_link lists
        discovery = [-1]*n
        low_link = [-1]*n
        time = 0
        res = []

# Assign discovery[v] and low_link[v] values.
# Recurse for all adjacent nodes.
# If an adjacent node u has been visited before and is not the direct parent, update low[v] to detect cycles.
# If low[u] > disc[v], then (v, u) is a bridge (critical connection).
        def dfs(node, parent):
            nonlocal time
            discovery[node] = time
            low_link[node] = time
            time+=1
            for ne in adj_list[node]:
                if ne==parent:continue
                if discovery[ne]==-1:
                    dfs(ne, node)
                    low_link[node] = min(low_link[node], low_link[ne])
                    if low_link[ne] > discovery[node]:
                        res.append([node, ne])
                else:
                    low_link[node] = min(low_link[node], discovery[ne])
 
        for i in range(n):
            if discovery[i]==-1:
                dfs(i, -1)
        return res        