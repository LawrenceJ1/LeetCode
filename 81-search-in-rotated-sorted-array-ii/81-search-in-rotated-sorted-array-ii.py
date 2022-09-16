class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if target in set(nums):
            return True
        return False