class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        for i in range(1, 10):
            cur = [i]
            for j in range(n-1):
                for l in range(len(cur)):
                    temp = cur[l]
                    if temp%10+k < 10 and temp%10-k >= 0:
                        cur[l]=temp*10+temp%10+k
                        cur.append(temp*10+temp%10-k)
                    elif temp%10+k < 10:
                        cur[l]=temp*10+temp%10+k
                    elif temp%10-k >= 0:
                        cur[l]=temp*10+temp%10-k
            for num in cur:
                if len(str(num)) == n:
                    ans.append(num)
        return list(set(ans))
                    
                            