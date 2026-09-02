class Solution:
    def trap(self, height: List[int]) -> int:

        max_left = float('-inf')
        max_right = float('-inf')

        left = 0
        right = len(height) - 1

        total_trapped = 0

        while left < right:

            max_left = max(height[left], max_left)
            max_right = max(height[right], max_right)

            water_level =min(max_left,max_right)


            if water_level > height[left] :
                trapped_water = water_level - height[left]
                total_trapped += trapped_water
            
            elif water_level > height[right]:
                trapped_water = water_level - height[right]
                total_trapped += trapped_water

            
            if height[right]> height[left]:
                left += 1
            
            else:
                right -=1
        
        return total_trapped