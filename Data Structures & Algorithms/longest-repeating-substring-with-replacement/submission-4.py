class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        l = 0
        res = 0
        maxFreq = 0
        for r in range (len(s)):
            window[s[r]] = 1 + window.get(s[r], 0) # get 0 if doesn't exist or +1
            maxFreq = max(maxFreq, window[s[r]])

            while(r-l+1) - maxFreq > k:
                window[s[l]] -= 1

                l +=1

            # size of the window = right - left + 1
            res = max(res, r-l + 1)

        return res

