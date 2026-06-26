class Solution:
    def reverseDegree(self, s: str) -> int:
        sums=0
        rever=['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
        for x in range(len(s)):
            sums+=(rever.index(s[x])+1)*(x+1)
            
        return sums
