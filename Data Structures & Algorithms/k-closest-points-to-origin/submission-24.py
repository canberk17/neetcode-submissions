from math import sqrt
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # heap=[]
        # origin=[0,0]

        # for point in points:
        #     distance=sqrt(pow(origin[0] - point[0],2) + pow(origin[1] - point[1],2))
        #     heapq.heappush(heap,(distance,point))

        # print(heap)
        # closest=[]

        # for _ in range(k):
        #     closest.append(heapq.heappop(heap)[1])
        

        # return closest

        def distance(point):
            x, y =point
            return x**2 + y**2
        
        def partition(l,r):
            pivotIdx = r
            pivot = distance(points[pivotIdx])
            i = l

            for j in range(l,r):
                if distance(points[j])<=pivot:
                    points[i],points[j] = points[j],points[i]
                    i+=1
            points[i],points[r] = points[r],points[i]

            return i
            
        L, R = 0, len(points) - 1
        pivot = len(points)

        while pivot != k:
            pivot = partition(L,R)
            if pivot < k:
                L = pivot + 1
            else:
                R = pivot -1
        return points[:k]
        

