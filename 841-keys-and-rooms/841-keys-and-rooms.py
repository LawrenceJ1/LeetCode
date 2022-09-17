class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False]*len(rooms)
        visited[0] = True
        keys = deque()
        for key in rooms[0]:
            keys.append(key)
        
        while keys:
            next_room = keys.pop()
            if visited[next_room] == True: continue
            else:
                visited[next_room] = True
                for key in rooms[next_room]:
                    keys.append(key)
        
        for i in visited:
            if i == False:
                return False
        return True