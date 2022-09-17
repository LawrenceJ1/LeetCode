class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        original = defaultdict(int)
        for s in s1:
            original[s] += 1
        perm = original.copy()
        count = counter = 0
        x = len(s1)
        y = len(set(s1))
        
        for i in range(len(s2)):
            if s2[i] in perm:
                if count == x:
                    if perm[s2[i-x]] == 0:
                        counter -= 1
                    perm[s2[i-x]] += 1
                    if perm[s2[i-x]] == 0:
                        counter += 1
                else:
                    count += 1
                if perm[s2[i]] == 0:
                    counter -= 1
                perm[s2[i]] -= 1
                if perm[s2[i]] == 0:
                    counter += 1
                if counter == y:
                    return True
            else:
                perm = original.copy()
                count = 0
                counter = 0
        return False