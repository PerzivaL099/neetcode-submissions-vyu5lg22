class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Create 2 pointers
        l = 0
        r = len(numbers) - 1
        # Iterate through list
        while l < r:
            #Sum of 2 pointers
            current_sum = numbers[l] + numbers[r]
             #logic to decide which pointer to move
            if current_sum > target:
                r -= 1
            elif current_sum < target:
                l += 1
            else:   
                #sum pair of indices
                return [l+1,r+1]