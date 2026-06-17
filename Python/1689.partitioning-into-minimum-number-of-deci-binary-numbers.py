class Solution:
    def minPartitions(self, n: str) -> int:
        ls=[]
        for x in range(len(n)):
            ls.append(n[x])
        return int(max(ls))
