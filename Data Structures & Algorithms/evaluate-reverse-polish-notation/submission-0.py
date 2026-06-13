class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for nums in tokens:
            if nums not in ("+", "-", "*", "/"):
                stack.append(int(nums))
                continue
            
            b = stack.pop()
            a = stack.pop()
            
            match nums:
                case "+":
                    stack.append(a + b)
                case "-":
                    stack.append(a - b)
                case "*":
                    stack.append(a * b)
                case "/":
                    stack.append(int(a / b))
            
        return stack[0]
