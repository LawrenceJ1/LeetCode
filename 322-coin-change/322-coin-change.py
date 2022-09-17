class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        queue = deque()
        visited = set()
        queue.append(0)
        ans = 1
        while queue:
            queue_len = len(queue)
            for i in range(queue_len):
                temp = queue.popleft()
                for coin in coins:
                    if coin + temp == amount:
                        return ans
                    elif coin + temp < amount and coin + temp not in visited:
                        queue.append(coin+temp)
                        visited.add(coin+temp)
            ans += 1
        return -1
    