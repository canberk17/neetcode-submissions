class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        counts = Counter(nums)

        index = 0

        for color in range(3):
            for _ in range(counts[color]):
                nums[index] = color
                index+=1
        

        
        
        

