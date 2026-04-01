class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Use a sliding window
        right = s[i+1]
        left = s[i]
        #hasmap for values
        uniqueValues = {}
        #iterate through string
        for char in s:
            if right != left:
                right = right[i+1]
                uniqueValues.append(right)
            elif right == left:
                left = left[i+1]
        return uniqueValues
        