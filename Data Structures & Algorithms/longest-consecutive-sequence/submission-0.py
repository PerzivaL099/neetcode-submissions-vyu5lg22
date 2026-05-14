class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #HashMap to store values
        numSet = set(nums)
        maxLength = 0

        #Loop through the set
        for n in numSet:
            
            if (n-1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                maxLength = max(maxLength, length)

        return maxLength


       
        