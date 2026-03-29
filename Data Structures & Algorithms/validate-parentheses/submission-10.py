class Solution:
    def isValid(self, s: str) -> bool:
        #HashMap for valid combinations
        pairs = {")": "(", "]": "[","}":"{"}
        #Implement Stack
        stack = []
        for char in s:
            if char in pairs:
                #Check if its a valid pair & take out
                if stack and stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                #when its not on stack
                stack.append(char)
        return not stack
            #if open char stack.push()
            #elif close char, 
                #stack.isEmpty() or stack.top != HashMap
                    #return False
            