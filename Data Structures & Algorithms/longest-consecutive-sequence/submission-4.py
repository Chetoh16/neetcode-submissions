class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)

        longest = 0

        # check if the number is the start by checking if it has a number smaller than it (by 1)
        # if not, it is the start.
        # then iteratively check if there is a number bigger than it (by 1) until you reach
        # the end of the sequence.

        for i in nums:
            # check if its the start of a sequence
            if (i-1) not in numSet:
                length = 0
                while (i + length) in numSet:
                    length += 1
                longest = max(length, longest)


        return longest