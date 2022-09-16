class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs[0]) == 0:
            return ""
        x = ""
        i = 0
        p = [strs[0][0]]
        while True:
            try:
                for j in range(len(strs)):
                    if strs[j][i] != p[i]:
                        return x
                x = "".join(p)
                i += 1
                p.append(strs[0][i])
            except:
                return x