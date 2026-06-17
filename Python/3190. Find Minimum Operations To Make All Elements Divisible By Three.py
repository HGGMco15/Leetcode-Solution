class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count=0
        for x in nums:
            if not x%3==0:
                count+=1
        return count
