class Solution:
    def isValid(self, s: str) -> bool:
        #HashMap for valid combinations
        pairs = {")": "(", "]": "[","}":"{"}
        #Implement Stack
        stack = []
        for char in s:
            if char in pairs:
                if stack and stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
            #if open char stack.push()
            #elif close char, 
                #stack.isEmpty() or stack.top != HashMap
                    #return False
            