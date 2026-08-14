class Solution:

    # first idea was to do NumWord so 5Hello5World, however this only works with
    # words < 2 digits. If there's => 2 digits, then add a # at the end of the numbers to signify its end

    def encode(self, strs: List[str]) -> str:

        encoded_m = []

        for i in strs:
            encoded_m.append(f"{len(i)}#{i}")
            # parts.append(f"{len(s)}#{s}") is faster bcs concat is less efficient 

        return "".join(encoded_m)



    def decode(self, s: str) -> List[str]:

        decoded_m = []

        i = 0
        
        while i < len(s):
            word_length = 0

            # print("i is: ", i)
            # print("word_l :", word_length)
            # print("s[i]:", s[i])

            while s[i] != "#":
                word_length = (word_length * 10) + (int(s[i]))

                # print("int(s[i])", int(s[i]))
                # print("new wl:", word_length)
                i = i + 1

            # print("s[i+1: word_length]:", s[i+1: word_length + i + 1])
            decoded_m.append(s[i+1: word_length + i + 1])
            i = i + 1 + word_length 
            # print("new i: ", i)
            # print("new decoded_m:", decoded_m)
        
        return decoded_m

