class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        #2 operations
            #1 step or 2 step
        n1 , n2 = 1, 2
        #Store operations in a list
        cache = []

        #2 recursirve calls
        for i in range(3, n+1):
            current = n1+n2
            n1 = n2
            n2 = current
        return n2
        

