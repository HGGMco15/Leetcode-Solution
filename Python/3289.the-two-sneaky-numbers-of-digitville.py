class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans=[]
        for x in nums:
            if nums.count(x)==2:
                ans.append(x)
        ans.sort()
        ls=set(ans)
        ans=list(ls)
        return ans
