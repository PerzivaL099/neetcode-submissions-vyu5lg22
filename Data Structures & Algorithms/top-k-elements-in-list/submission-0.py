class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #HashMap to store frequency
        frequencies = {}
        #Bucket List
        for n in nums:
            frequencies[n] = 1 + frequencies.get(n,0)

        freq = [[] for i in range(len(nums)+ 1)]
        for n,c in count.items():
            freq[c].append(n)
        #Iterate through array
            #K indicator of how many values return
        res = []

        for i in range(len(freq) -1,0,-1):
            for n in freq[i]:
                res.append(n)
                #if we already have k values
                if len(res) == k:
                    return res

        #return highest appeared value
            #repeat until k conditional is complete