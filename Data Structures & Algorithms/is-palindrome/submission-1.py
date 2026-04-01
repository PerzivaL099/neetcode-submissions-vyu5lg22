class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Pointers
        l = 0
        r = len(s) - 1
        #Iterate through len
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -+ -1
                if s == l:
                    return true
            #compare values of pointers
            #return true if palindrome
        return false
        #return false if no match