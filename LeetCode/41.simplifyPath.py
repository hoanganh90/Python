class Solution:
    def simplifyPath(self, path: str) -> str:
        result = []
        diractories = path.split("/")
        for dir in diractories:
            if dir == "." or not dir:
                continue
            elif dir == "..":
                if result:
                    result.pop()
            else:
                result.append(dir)
        return "/" + "/".join(result)
s = Solution()
print(s.simplifyPath("/home/..../../foo/"))
                    