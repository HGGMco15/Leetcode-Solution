class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        a=nums
        ans=[]
        for x in a:
            if x%2==0:
                ans.append(0)
            else:
                ans.append(1)
        ans.sort()
        return ans
