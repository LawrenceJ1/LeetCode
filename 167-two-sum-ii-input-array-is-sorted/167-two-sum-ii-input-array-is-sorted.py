class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = 0
        b = -1
        while numbers[a] + numbers[b] != target:
            if numbers[a] + numbers[b] > target:
                b -= 1
            else:
                a += 1
        return [a+1,len(numbers)+b+1]