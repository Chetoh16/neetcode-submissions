class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        foundDuplicate = False

        dictionary = {}
        for item in nums:
            if item in dictionary:
                foundDuplicate = True
            else:
                dictionary[item] = item

        return foundDuplicate