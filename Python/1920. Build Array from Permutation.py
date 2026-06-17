class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ls=[]
        for x in range(len(nums)):
            ls.append(nums[nums[x]])

        return ls
