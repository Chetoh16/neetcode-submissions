class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        

        # initial idea:
        # make 2 hash maps, and map each char to a value (how many times it appears)
        # if both hash maps have same values for all keys, it's an anagram
        dic1 = {}
        
        dic2 = {}

        for char in s:
            if char in dic1:
                dic1[char] += 1
            else:
                dic1[char] = 0
        
        for char in t:
            if char in dic2:
                dic2[char] += 1
            else:
                dic2[char] = 0
        
        print(dic1)
        print(dic2)
        
        for item in dic1:
            if item in dic2:
                if dic1[item] != dic2[item]:
                    return False
            else:
                return False
        
        return True