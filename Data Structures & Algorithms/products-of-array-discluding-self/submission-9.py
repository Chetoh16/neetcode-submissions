class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        output = [0] * len(nums)

        n = len(nums) - 1
        
        for i in range(len(nums)):

            if(i == 0 or n == len(nums) -1):
                prefix[i] = nums[i]
                postfix[n] = nums[n]
            else:
                prefix[i] = nums[i] * prefix[i-1]
                postfix[n] = nums[n] * postfix[n+1]

            n = n-1
        
        
        for i in range(len(nums)):
            if(i == 0):
                output[i] = postfix[i+1]
            elif(i == len(nums)-1):
                print(i)
                output[i] = prefix[i-1]
            else:
                output[i] = prefix[i-1] * postfix[i+1]

        return output

            

