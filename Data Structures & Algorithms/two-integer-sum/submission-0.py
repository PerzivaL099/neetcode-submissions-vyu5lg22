class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {}
        for i, n in enumerate(nums):
            #Number needed to reach target
            #By summing it to actual number
            complement = target - nums[i]
            #If we already have it, return the list
            if complement in seen_map:
                #List with complement and current index
                return [seen_map[complement], i]

            #Add current number and index to map
            seen_map[n] = i