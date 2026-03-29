class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #HashMap to store new sublist
        subAnagrams = defaultdict(list)
        #Iterate through each strs
        for s in strs:
            #Order them in alphabetical order
            sorted_s = "".join(sorted(s))
        
        
            #Append to subAnagrams
            subAnagrams[sorted_s].append(s)

        return list(subAnagrams.values())