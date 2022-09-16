class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        c = -1
        while digits[c] == 10:
            try:
                digits[c-1] += 1
            except:
                digits.insert(0, 1)
            digits[c] = 0
            c -= 1
        return digits