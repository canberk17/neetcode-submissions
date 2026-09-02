from math import sqrt
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        origin=[0,0]

        for point in points:
            distance=sqrt(pow(origin[0] - point[0],2) + pow(origin[1] - point[1],2))
            heapq.heappush(heap,(distance,point))

        print(heap)
        closest=[]

        for _ in range(k):
            closest.append(heapq.heappop(heap)[1])
        

        return closest