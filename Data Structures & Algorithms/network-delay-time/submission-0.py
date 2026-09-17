class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}

        for i in range (1, n + 1):
            adj[i]= []

        
        for src, dst, time in times:
            adj[src].append((dst,time))
        
        heap = [(0,k)]
        shortest = {}

        while heap:
            time, node = heapq.heappop(heap)

            if node in shortest:
                continue
            
            shortest[node] = time

            for nei, edge_time in adj[node]:
                if nei not in shortest:
                    heapq.heappush(heap,(time + edge_time, nei))
            

        if len(shortest) != n:
            return -1
        
        return max(shortest.values())