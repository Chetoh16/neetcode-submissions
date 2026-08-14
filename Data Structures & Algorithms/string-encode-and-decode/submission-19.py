class Solution:

    # first idea was to do NumWord so 5Hello5World, however this only works with
    # words < 2 digits. If there's => 2 digits, then add a # at the end of the numbers to signify its end

    def encode(self, strs: List[str]) -> str:

        encoded_m = []

        for i in strs:
            encoded_m.append(f"{len(i)}#{i}")
            # encoded_m.append(f"{len(s)}#{s}") is faster bcs concat is less efficient 

        return "".join(encoded_m)



    def decode(self, s: str) -> List[str]:

        decoded_m = []

        i = 0
        
        while i < len(s):
            word_length = 0

            while s[i] != "#":

                # calculate the word length by taking one int at a time 
                # i.e. "123"
                # word_length = (0 * 10) + 1 = 1
                # word_length = (1 * 10) + 2 = 12
                # word_length = (12 * 10) + 3 = 123
                word_length = (word_length * 10) + (int(s[i]))
                i = i + 1

            # split the word from right after the # and for word_length + i + 1 characters (+1 bcs it's exclusive)
            # 3#ege5#cetin
            # ['ege', 'cetin']
            decoded_m.append(s[i+1: word_length + i + 1])

            # get i back on track (right after where the word ends)
            i = i + 1 + word_length 
        
        return decoded_m

