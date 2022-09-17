class Solution:
    def calculate(self, s: str) -> int:
        ans = deque()
        num = 0
        oper = "+"
        for char in s:
            if char == " ":
                continue
            elif char.isdigit():
                num = num*10+int(char)
            else:
                if oper == "+":
                    ans.append(num)
                elif oper == "-":
                    ans.append(-num)
                elif oper == "*":
                    ans.append(ans.pop()*num)
                else:
                    ans.append(int(ans.pop()/num))
                oper = char
                num = 0
        if oper == "+":
            ans.append(num)
        elif oper == "-":
            ans.append(-num)
        elif oper == "*":
            ans.append(ans.pop()*num)
        else:
            ans.append(int(ans.pop()/num))
        a = sum(ans)
        return a