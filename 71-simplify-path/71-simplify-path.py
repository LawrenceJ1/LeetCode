class Solution:
    def simplifyPath(self, path: str) -> str:
        can_path = path.split("/")
        ans = deque()
        ans.append("")
        for word in can_path:
            if word == "..":
                ans.pop()
                if not ans:
                    ans.append("")
            elif word == "." or word == "":
                continue
            else:
                ans.append(word)
        return "/".join(ans) or "/"