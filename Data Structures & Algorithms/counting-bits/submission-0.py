class Solution:
    def countBits(self, n: int) -> List[int]:
        
        result = []
        def countbits(n):
            count = 0 

            while n > 0:
                if n & 1 == 1:
                    count+=1
                n = n >> 1
            return count
        for num in range(n + 1):
            result.append(countbits(num))
        
        return result