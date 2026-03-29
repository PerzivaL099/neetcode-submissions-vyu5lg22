class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Store visited in set
        visited = set()
        #Edge case array is empty
        for n in nums:
            if n in visited:
                return True
            else:
                visited.add(n)

        #If no duplicates are found
        return False

    




