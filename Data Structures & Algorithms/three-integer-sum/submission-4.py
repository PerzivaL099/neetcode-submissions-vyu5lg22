class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Sort array
        nums.sort()
        result = []
        #Iterate through array
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            #Find 2 values that make a = 0 
            l = i+1
            r = len(nums) - 1
            #Use logic of 2 sum = target
            #In this case target = a -> 0
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return result