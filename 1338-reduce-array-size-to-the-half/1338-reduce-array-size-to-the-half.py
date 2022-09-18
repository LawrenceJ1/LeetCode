class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dictionary = defaultdict(int)
        for num in arr:
            dictionary[num] += 1
        size = len(arr)
        count = 0
        half = len(arr)//2
        for value in sorted(dictionary.values(), reverse=True):
            size -= value
            count += 1
            if size <= half:
                return count
        return count