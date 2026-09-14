class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * (n+1)
        def memoization(n,):
            if n<= 1:
                return 1
            
            if cache[n] != -1:
                return cache[n]
            
            cache[n] = memoization(n-1) + memoization(n-2)

            return cache[n]
        
        return memoization(n)