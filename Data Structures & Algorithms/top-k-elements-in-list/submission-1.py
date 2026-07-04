class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = 1+ count.get(i,0)
        freq = [[] for i in range(len(nums)+ 1)]
        for num, c in count.items():
            freq[c].append(num)
        res = []
        for j in range(len(freq) -1 , 0, -1):
            for n in freq[j]:
                res.append(n)
                if len(res) == k:
                    return res
