class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        left=1

        for right in range(1,len(nums)):

            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left += 1
        return left

        # i = 0

        # while i < len(nums):
        #     if nums[i] in nums[:i]:
        #         nums.pop(i)
        #     else:
        #         i+=1
        # return len(nums)
        
        # l=1 

        # for r in range(1,len(nums)):
        #     if nums[r]!=nums[r-1]:
        #         nums[l]=nums[r]
        #         l+=1
        # return l

        
