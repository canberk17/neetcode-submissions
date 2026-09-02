class Solution:
    def isPalindrome(self, x: int) -> bool:
        number =str(x)
        left = 0
        right = len(number) - 1

        while left < right:
            if number[left] != number[right]:
                return False
            
            left += 1
            right -=1
        return True