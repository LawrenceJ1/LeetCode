class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for x in tokens:
            if x == "+" or x == "-" or x=="*" or x=="/":
                second = int(stack.pop())
                first = int(stack.pop())
                if x == "+":
                    stack.append(first+second)
                elif x == "-":
                    stack.append(first-second)
                elif x == "*":
                    stack.append(first*second)
                else:
                    stack.append(int(first/second))
            else:
                stack.append(int(x))
        return stack[0]