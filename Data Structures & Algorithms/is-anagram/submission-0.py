class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Edge Case if both str are not same length
        if len(s) != len(t):
            return False
        #Use HashMaps
        countS = {}
        countT = {}
        #Iterate through str
        for i in range(len(s)):
            #get char from stirng and add to dict
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)

        return countS == countT