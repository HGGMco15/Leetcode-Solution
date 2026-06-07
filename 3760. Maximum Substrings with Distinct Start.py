class Solution:
    def maxDistinct(self, s: str) -> int:
        ls=[]
        for x in range(len(s)):
            if not s[x] in ls:
                ls.append(s[x])
        return len(ls)
