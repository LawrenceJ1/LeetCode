class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque() #used to store the indices to travel to
        visited = set()
        queue.append(start)  
        visited.add(start) #keeps track of the visited indices
        arr_len = len(arr)
        while queue:
            index = queue.popleft()
            val = arr[index]
            if val == 0:
                return True
            plus = val+index
            minus = index-val
            if plus not in visited and plus < arr_len:
                queue.append(plus)
                visited.add(plus)                
            if minus not in visited and minus > -1:
                queue.append(minus)
                visited.add(minus)
        return False