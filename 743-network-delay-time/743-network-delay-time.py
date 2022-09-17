class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        queue = deque()
        d = {}
        signal_time = [inf]*(n+1)
        for t in times:
            if t[0] not in d:
                d[t[0]] = []
            d[t[0]].append([t[1], t[2]])
        queue.append(k)
        signal_time[k] = 0
        signal_time[0] = 0
        while queue:
            l = len(queue)
            for i in range(l):
                x = queue.popleft()
                if x not in d:
                    continue
                for t in d[x]:
                    if signal_time[x]+t[1] < signal_time[t[0]]:
                        queue.append(t[0])
                        signal_time[t[0]] = signal_time[x]+t[1]
        if max(signal_time) == inf:
            return -1
        return max(signal_time)