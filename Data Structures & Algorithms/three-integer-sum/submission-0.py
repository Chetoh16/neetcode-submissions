class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):

            # since it's sorted, if it doesn't start with a > 0 num, it means there are only
            # pos ints which means they can't add up to 0
            if a > 0:
                break
            
            if i > 0 and a == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) -1

            while left < right:
                threeSum = a + nums[left] + nums[right]
                
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        
        return res