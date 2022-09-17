class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if not k%2 or not k%5:
            return -1
        n=length=1
        while True:
            n=n%k
            if not n:
                return length
            length += 1
            n = n*10+1
        