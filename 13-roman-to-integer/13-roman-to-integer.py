class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        length = len(s)
        i = 0
        while i < length:
            if s[i] == "I":
                ans += 1
                if i+1 < length:
                    if s[i+1] == "V":
                        ans += 3
                        i += 1
                    elif s[i+1] == "X":
                        ans += 8
                        i += 1
            elif s[i] == "X":
                ans += 10
                if i+1 < length:
                    if s[i+1] == "L":
                        ans += 30
                        i += 1
                    elif s[i+1] == "C":
                        ans += 80
                        i += 1
            elif s[i] == "C":
                ans += 100
                if i+1 < length:
                    if s[i+1] == "D":
                        ans += 300
                        i += 1
                    elif s[i+1] == "M":
                        ans += 800
                        i += 1
            elif s[i] == "V":
                ans += 5
            elif s[i] == "L":
                ans += 50
            elif s[i] == "D":
                ans += 500
            else:
                ans += 1000
            i += 1
        return ans
                    
                