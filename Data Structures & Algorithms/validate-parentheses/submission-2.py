class Solution:
    def isValid(self, s: str) -> bool:
        #HashMap for valid combinations
        map = {")": ")", "]": "[","{}":"}"}
        #Implement Stack
        stack = []
        for char in s:
            if char in map:
                if stack and stack[-1] == map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append
        return True if not stack else False
            #if open char stack.push()
            #elif close char, 
                #stack.isEmpty() or stack.top != HashMap
                    #return False
            