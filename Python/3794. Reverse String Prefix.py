class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        ls=[]
        ls2=[]
        for x in range(len(s)):
            if x<k:
                ls.append(s[x])
            else:
                ls2.append(s[x])
        ls.reverse()
        res="".join(ls)
        res2="".join(ls2)


        return res+res2
