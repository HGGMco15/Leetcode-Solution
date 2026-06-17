class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ls=[]
        for x in range(len(jewels)):
            if jewels[x] not in ls:
                ls.append(jewels[x])
        
        a=stones
        count=0
        for y in ls:
            count+=a.count(y)

        return count
