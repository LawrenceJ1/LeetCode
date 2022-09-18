class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ret = ["a"]*n
        count = n
        pos = -1
        while count < k:
            if count+25 < k:
                ret[pos] = "z"
                pos -= 1
                count += 25
            else:
                ret[pos] = chr(97+k-count)
                count += k-count
        return "".join(ret)