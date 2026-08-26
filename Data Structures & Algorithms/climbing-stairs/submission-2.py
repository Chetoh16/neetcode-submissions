class Solution:
        
    def climbStairs(self, n: int) -> int:
        
        ways = 0

        # (1 = 1)
        # 1 = 1
        # 2 = 2
        # 3 = 3
        # 4 = 5
        # 5 = 8
        # 6 = 13
        # 7 = 21
        # 8 = 34
        # 9 = 55

        # oh wow it's the fibonnaci sequence

        if n in [1,2,3]:
            print("returning")
            return n

        prev1 = 3
        prev2 = 2
        for i in range(3, n, 1):

            
            print("prev1", prev1)
            print("prev2", prev2)
            ways = prev1 + prev2
            print("ways", ways)
            prev2 = prev1
            prev1 = ways


            

        return ways


    