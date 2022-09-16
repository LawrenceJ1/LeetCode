class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        nums = deque()
        s = deque(s.lstrip())
        j = 0
        if len(s) == 0:
            return 0
        if s[0] == "-":
            nums.append("-")
        if s[0] in ["+", "-"]:
            s.popleft()
        while j < len(s):
            if s[j] == "0":
                s.popleft()
            else:
                break
        for i in s:
            if i.isdigit():
                nums.append(i)
            else:
                break
        if not nums:
            return 0
        if len(nums) == 1 and (nums[0] == "+" or nums[0] == "-"):
            return 0
        return max(-2**31, min(int("".join(nums)), 2**31-1))