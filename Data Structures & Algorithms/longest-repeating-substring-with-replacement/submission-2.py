class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Sliding window 
        left = 0
        #HashMap frequencies
        frequencies = {}
        max_f = 0
        max_len = 0

        for right in range(len(s)):
            #Update frquencie of current character
            char = s[right]
            frequencies[char] = 1 + count.get(char,0)

            #Update most frequent character
            max_f = max(max_f, count[char])

            #validate size of window
            while (right - left + 1) - max_f > k:
                #if not valid 
                count[s[left]] -= 1
                left += 1
            #calculate max
            max_len = max(max_len, right - left + 1)
        return max_len