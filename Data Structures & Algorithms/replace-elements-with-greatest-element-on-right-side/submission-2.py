class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        max_from_right = -1


        for i in reversed(range(len(arr))):
            current = arr[i]

            arr[i] = max_from_right

            if current > max_from_right :
                max_from_right = current
        

        return arr



            
        