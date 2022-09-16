class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = set()
        def backtrack(para=[], unclosed=0, num=0):
            if num == n:
                for i in range(unclosed):
                    para.append(")")
                self.ans.add("".join(para))
            else:
                backtrack(para[:]+["("],unclosed+1,num+1)
                backtrack(para[:]+["()"],unclosed,num+1)
                temp = para[:]
                for i in range(unclosed):
                    temp.append(")")
                    backtrack(temp[:]+["("],unclosed-i,num+1)
        backtrack()
        return list(self.ans)