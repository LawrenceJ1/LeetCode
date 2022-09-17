class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        d = False
        if len(arr) == 1 or len(arr) == 2:
            return False
        if arr[0] > arr[1]:
            return False
        for i in range(len(arr)-1):
            if d:
                if arr[i] <= arr[i+1]:
                    return False
            else:
                if arr[i] > arr[i+1]:
                    d = True
                if arr[i] == arr[i+1]:
                    return False
        if not d:
            return False
        return True