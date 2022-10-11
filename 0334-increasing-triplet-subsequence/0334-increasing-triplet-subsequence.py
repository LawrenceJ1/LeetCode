class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        smaller = []
        smallest = inf
        larger = deque()
        largest = -inf
        for i in range(len(nums)):
            if nums[i] <= smallest:
                smallest = nums[i]
                smaller.append(False)
            else:
                smaller.append(True)
            if nums[-i-1] >= largest:
                largest = nums[-i-1]
                larger.appendleft(False)
            else:
                larger.appendleft(True)
        for i in range(len(nums)):
            if smaller[i] and larger[i]:
                return True
        return False