class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        ans = 0
        max_defense = 0
        properties.sort(key=lambda x: (-x[0],x[1]))
        for _, defense in properties:
            if defense < max_defense:
                ans += 1
            else:
                max_defense = defense
        return ans