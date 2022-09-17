class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ans = 0
        new = defaultdict(int)
        for num1 in nums1:
            for num2 in nums2:
                new[num1+num2] += 1
        for num3 in nums3:
            for num4 in nums4:
                ans += new[0 - (num3+num4)]
        return ans