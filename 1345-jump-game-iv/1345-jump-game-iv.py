class Solution:
    def minJumps(self, arr: List[int]) -> int:
        x = len(arr)
        if x == 1:
            return 0
        
        indices = {}
        visited = set()
        queue = deque()
        counter = 0
        queue.append(0)
        visited.add(0)
        
        for i in range(x):
            if arr[i] not in indices:
                indices[arr[i]] = []
            indices[arr[i]].append(i)

        while True:
            queue_len = len(queue)
            for i in range(queue_len):
                pos = queue.popleft()
                if pos == x-1:
                    return counter 
                if (pos+1) not in visited:
                    queue.append(pos+1)
                    visited.add(pos+1)
                if (pos-1)>=0 and (pos-1) not in visited:
                    queue.append(pos-1)
                    visited.add(pos-1)
                for i in indices[arr[pos]]:
                    if i not in visited:
                        queue.append(i)
                        visited.add(i)
                indices[arr[pos]].clear()
            counter += 1
                