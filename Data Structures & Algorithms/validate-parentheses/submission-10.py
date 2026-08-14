class Solution:
    def isValid(self, s: str) -> bool:
        
        closed_br = [')', '}', ']']

        # check if it's not even or starting with closed brackets
        if (len(s) % 2) != 0 or s[0] in closed_br:
            return False
        
        l = list(s)

        stack = []

        for i in range(len(l)):
            if l[i] not in closed_br:
                stack.append(l[i])
                print("append l[%d]: %c to stack" % (i,l[i]))
                print("new stack:", stack)
                continue
            if l[i] == ')' and (not stack or stack[-1] != '('):
                print("not ()")
                return False
            elif l[i] == ']' and (not stack or stack[-1] != '['):
                print("not []")
                return False
            elif l[i] == '}' and (not stack or stack[-1] != '{'):
                print("not {}")
                return False
            print("pop stack")
            stack.pop()
        
        if(stack):
            return False
        




        return True
             