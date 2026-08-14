class Solution:
    def isValid(self, s: str) -> bool:
        
        closed_br = [')', '}', ']']

        # check if it's not even or starting with closed brackets
        if (len(s) % 2) != 0 or s[0] in closed_br:
            return False
        
        stack = []

        # go through the entire string
        for i in range(len(s)):

            # if the char is not a close bracket, add it to the stack
            # this way, when you see a close bracket, the top of the stack has to be the open version of the same bracket
            if s[i] not in closed_br:
                stack.append(s[i])
                # print("append l[%d]: %c to stack" % (i,l[i]))
                # print("new stack:", stack)
                continue
            
            # check if ast bracket in string/list matches the top of the stack
            # extra check to see if the stack is empty while there is a close bracket
            if s[i] == ')' and (not stack or stack[-1] != '('):
                # print("not ()")
                return False
            elif s[i] == ']' and (not stack or stack[-1] != '['):
                # print("not []")
                return False
            elif s[i] == '}' and (not stack or stack[-1] != '{'):
                # print("not {}")
                return False

            # print("pop stack")
            stack.pop()

        # the stack must be empty at the end
        return not stack
             