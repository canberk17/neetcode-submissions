class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts= Counter(nums)
        res = []

        for freq in counts.most_common(k):
            res.append(freq[0])
        
        return res
