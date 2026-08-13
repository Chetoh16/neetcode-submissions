class Solution:
    def isPalindrome(self, s: str) -> bool:


        # strip spaces and non alphanumeric characters
        ns = ''.join(filter(str.isalnum, s)).lower()
        # print(ns)

        midway = len(ns) // 2
        # print(midway)

        for i in range(midway):
            # print(i)
            # print("beginning:", ns[i])
            # print("end: ", ns[len(ns)-i-1])
            if ns[i] != ns[len(ns)-i-1]:
                return False

        return True
        



