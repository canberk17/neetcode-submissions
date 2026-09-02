class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        l=0

        for r in range(len(nums)):
            if nums[r] != val:
                nums[l]=nums[r]
                l+=1
        return l
        # i=0

        # while i < len(nums):

        #     if nums[i]==val:
        #         nums.pop(i)
        #     else:
        #         i+=1
        # return len(nums)
        # for i in range(len(nums)-1,-1,-1):
        #     if nums[i]==val:
        #         nums.pop(i)
        # return len(nums)