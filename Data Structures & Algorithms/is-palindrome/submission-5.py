class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ""
        for char in s:
            if char.isalnum():
                clean_s += char.lower()
        #Pointers
        l = 0
        r = len(clean_s) - 1
        #Iterate through len
        while l < r:
            if clean_s[l] != clean_s[r]:
                return false
            l += 1
            r -+ -1
                  
            #compare values of pointers
            #return true if palindrome
        return True
        #return false if no match