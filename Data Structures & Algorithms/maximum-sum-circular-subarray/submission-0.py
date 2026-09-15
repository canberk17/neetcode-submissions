class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = nums[0]
        minSum = nums[0]

        currMax = 0
        currMin = 0

        total = 0

        for n in nums:
            currMax = max(currMax + n ,n)
            maxSum = max(maxSum,currMax)

            currMin = min(currMin + n, n)
            minSum = min(currMin,minSum)

            total += n
        
        if maxSum < 0:
            return maxSum
        
        return max(maxSum, total - minSum)