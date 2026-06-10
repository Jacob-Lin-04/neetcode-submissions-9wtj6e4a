class Solution:
    def isValid(self, s: str) -> bool:
        #dict map of closing brackets to its opening par
        brackets = { ')':'(', '}':'{', ']':'['}

        stack = list()

        for n in s:
            if n in brackets: # its a closing bracket
                # stack is empty or top doesnt match
                if not stack or stack[-1] != brackets[n]:
                    return False
                # removed matched opening bracket
                stack.pop()

            else: # it is an opening bracket
                stack.append(n)
          
        # valid only if all brakctes are matched so stack is empty
        return len(stack) == 0