class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        x = len(jobDifficulty)
        if x < d:
            return -1
        
        hardest_job_remaining = [0] * x
        hardest_job = 0
        for i in range(x - 1, -1, -1):
            hardest_job = max(hardest_job, jobDifficulty[i])
            hardest_job_remaining[i] = hardest_job
        
        @lru_cache(None)
        def dp(i, day):
            if day==d:
                return hardest_job_remaining[i]
            y = float(inf)
            hardest = 0
            for j in range(i, x-(d-day)):
                hardest = max(jobDifficulty[j], hardest)
                y = min(dp(j+1, day+1)+hardest, y)
            return y
        return dp(0, 1)
        