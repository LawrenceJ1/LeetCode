class Solution:
    def minDeletions(self, s: str) -> int:
        ans = [0]*26
        for char in s:
            ans[ord(char)-97] += 1
        ans.sort()
        pointer = 0
        for i in range(26):
            if ans[i] != 0:
                pointer = i
                break
        count = 0
        start = pointer
        while pointer < len(ans):
            if pointer+1 < len(ans) and ans[pointer] == ans[pointer+1]:
                ans[pointer] -= 1
                count += 1
                if ans[pointer] == 0:
                    start = pointer+1
                elif pointer-1 >= start:
                    pointer -= 1
            else:
                pointer += 1
        return count
                
            
                        