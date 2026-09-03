class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        queue = deque()
        ans = []
        left = 0

        for right in range(len(nums)):

            while queue and nums[right] > nums[queue[-1]]:
                queue.pop()
            
            queue.append(right)

            if left > queue[0]:
                queue.popleft()
            
            if right + 1 >= k:
                ans.append(nums[queue[0]])
                left+=1
        
        return ans
