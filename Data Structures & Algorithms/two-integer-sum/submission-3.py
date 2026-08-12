class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # initial idea:
        # have a dictionary of items. 
        # for each item, starting from dic[0], check target - dic [0] to see if that number exists.
        dic = {}

        # n = value, i = index
        for i, n in enumerate(nums):
            dic[n] = i

        for i, n in enumerate(nums):
            difference = target - n
            if difference in dic and dic[difference] != i:
                return [i, dic[difference]]
    
        return []





