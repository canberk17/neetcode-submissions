class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        L = 0
        max_freq = 0
        longest = 0

        for R in range(len(s)):
            counts[s[R]] = counts.get(s[R], 0) + 1

            max_freq = max(max_freq, counts[s[R]])

            while (R - L + 1) - max_freq > k:
                counts[s[L]] -= 1
                L += 1
            
            longest = max(longest, R - L + 1)

        
        return longest