from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
            
        counterS= Counter(s)
        counterT= Counter(t)


        for c in counterS:
            if counterS[c] != counterT.get(c,0):
                return False
        return True
