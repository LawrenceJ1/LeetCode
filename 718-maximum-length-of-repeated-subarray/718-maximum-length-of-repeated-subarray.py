class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        memo = [[0] * (len(nums2)+1) for _ in range(len(nums1)+1)]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    memo[i+1][j+1] = memo[i][j]+1
        return max(max(x) for x in memo)