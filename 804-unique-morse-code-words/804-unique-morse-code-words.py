class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        keys = {}
        ans = set()
        count = 0
        keys["a"] = ".-"
        keys["b"] = "-..."
        keys["c"] = "-.-."
        keys["d"] = "-.."
        keys["e"] = "."
        keys["f"] = "..-."
        keys["g"] = "--."
        keys["h"] = "...."
        keys["i"] = ".."
        keys["j"] = ".---"
        keys["k"] = "-.-"
        keys["l"] = ".-.."
        keys["m"] = "--"
        keys["n"] = "-."
        keys["o"] = "---"
        keys["p"] = ".--."
        keys["q"] = "--.-"
        keys["r"] = ".-."
        keys["s"] = "..."
        keys["t"] = "-"
        keys["u"] = "..-"
        keys["v"] = "...-"
        keys["w"] = ".--"
        keys["x"] = "-..-"
        keys["y"] = "-.--"
        keys["z"] = "--.."
        for word in words:
            transform = ""
            for char in word:
                transform += keys[char]
            if transform not in ans:
                count += 1    
            ans.add(transform)
        return count