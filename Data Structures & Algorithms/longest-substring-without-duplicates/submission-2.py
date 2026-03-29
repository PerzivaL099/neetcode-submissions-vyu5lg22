class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Use a sliding window
        max_len = 0
        left = 0
        #hasmap for values
        char_set = set()
        #iterate through string
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            #Add new character and get len of window
            char_set.add(s[right])
            max_len = max(max_len, right - left +1)

        return max_len