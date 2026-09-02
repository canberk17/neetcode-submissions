class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closeToOpen= {')':'(',']':'[','}':'{'}

        for char in s:
            if char in closeToOpen:
                if stack and stack[-1]==closeToOpen[char]:
                    stack.pop()
                else: # if stack is empty or open parenthesis dont match
                    return False
            else: # then its a open parenthesis
                stack.append(char)
        return True if not stack else False