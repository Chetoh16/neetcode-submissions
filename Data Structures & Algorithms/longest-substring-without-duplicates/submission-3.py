class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # set to make sure there are no duplicates
        duplicate = set()
        longest = 0
        # left pointer
        l = 0
        
        # right pointer
        for r in range(len(s)):

            while s[r] in duplicate:
                duplicate.remove(s[l])
                l += 1

            # add to set
            duplicate.add(s[r])

            # r-l for the range, +1 bcs its 0 indexed
            longest = max(longest, r-l + 1)


        return longest