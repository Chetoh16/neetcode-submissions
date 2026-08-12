class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list)

        # empty or singleton
        if len(strs) <= 1:  
            return [strs]
        
        for s in strs:
            count = [0] * 26 

            for c in s:
                count[ord(c) - ord("a")] += 1
                # print(count)
                # the key is the mapping to the alphabet
                # i.e. bab = 1a,2b,0c,0d... = [1,2,0,0...]

            # tuple
            result[tuple(count)].append(s)

        return list(result.values())