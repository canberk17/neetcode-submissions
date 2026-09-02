class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()

        left =0

        curr = 0
        longest = 0

        for right in range(len(s)):

            while s[right] in seen:
                left_char = s[left]
                seen.remove(left_char)
                curr -= 1
                left += 1
            
            seen.add(s[right])
            curr += 1
            longest= max(longest,curr)

        return longest


            
            


            