class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check the length of both strings first
        # if theyre not the same length
        # we know its false without doing anything else
        if len(s) != len(t):
            return False
        
        sMap, tMap = {}, {}

        # building hashmaps
        for i in range(len(s)):
            # if key does not exist in hashmap
            # default value is 0
            # sMap.get(s[i], 0)

            sMap[s[i]] = 1 + sMap.get(s[i], 0)
            tMap[t[i]] = 1 + tMap.get(t[i], 0)
        
        # iterating through keys in sMap
        for c in sMap:
            # what if the key doesn't exit in t Map?
            if sMap[c] != tMap.get(c, 0):
                return False

        return True


        


        