class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque()
        step = 0
        if target == "0000":
            return 0
        queue.append("0000")
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        deadends.add("0000")
        while queue:
            step += 1
            queue_length = len(queue)
            for x in range(queue_length):
                for y in range(4):
                    new_value = ""
                    new_combination = ""
                    
                    new_value = (int(queue[0][y])+1)%10
                    new_combination = queue[0][:y]+str(new_value)+queue[0][y+1:]
                    
                    if new_combination == target:
                        return step
                    if new_combination not in deadends:
                        queue.append(new_combination)
                        deadends.add(new_combination)
                    
                    new_value = (int(queue[0][y])-1)%10
                    new_combination = queue[0][:y]+str(new_value)+queue[0][y+1:]
                    
                    if new_combination == target:
                        return step
                    if new_combination not in deadends:
                        queue.append(new_combination)
                        deadends.add(new_combination)
                    
                queue.popleft()
        return -1
            