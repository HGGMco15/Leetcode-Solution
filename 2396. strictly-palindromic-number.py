class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def check(m):
            nums=str(m)
            return nums==nums[::-1]
        
        for x in range(2,n+10):   
            if check(x)==False:
                return False
        return True
