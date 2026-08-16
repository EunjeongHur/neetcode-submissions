class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for item in tokens:
            if item not in ["+", "-", "*", "/"]:
                stack.append(int(item))
            else:
                second_val = int(stack.pop())
                first_val = int(stack.pop())
                current_val = 0
                if item == "+":
                    current_val = first_val + second_val
                elif item == "-":
                    current_val = first_val - second_val
                elif item == "*":
                    current_val = first_val * second_val
                else:
                    current_val = first_val / second_val
            
                stack.append(current_val)
        return int(stack[0])
                    