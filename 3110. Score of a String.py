class Solution:
    def scoreOfString(self, s: str) -> int:
        su=0
        count=1
        for x in range(len(s)-1):
            a=abs(ord(s[x])-ord(s[x+1]))
            su+=a
        return su
