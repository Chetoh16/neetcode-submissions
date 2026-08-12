class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        # initial idea:
        # key = number, value = # of times it appears
        # find max, and loop k times and remove max to find new max each time
        dic = {}
        for items in nums:
            if items in dic:
                dic[items] += 1
            else:
                dic[items] = 1
        # another way to write this is 
        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)


        #print(dic)

        largest = []
        for i in range(k):
            
            max_num = max(dic, key=dic.get)
            #print("max num=", max_num)

            largest.append(max_num)
            #print("largest - current index:",i)
            #print("largest list", largest)

            dic.pop(max_num)
            #print("dic after removing max_num: ", dic)

        return largest
