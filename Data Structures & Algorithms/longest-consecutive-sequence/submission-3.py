class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        # easiest option:
        # sort the array, count length of consecutive sequences and output max one
        nums.sort() 
        print(nums)

        longest = 0
        temp_longest = 1
        for i in range(len(nums)-1):
        
            if nums[i] == nums[i+1] - 1:
                temp_longest = temp_longest + 1
                continue
            elif nums[i] == nums[i+1]:
                continue
            if temp_longest >= longest:
                longest = temp_longest
                temp_longest = 1


        return temp_longest if (temp_longest > longest) else longest