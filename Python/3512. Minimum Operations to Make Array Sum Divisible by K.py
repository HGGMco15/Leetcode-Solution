class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        a=sum(nums)
        count=0
        if a%k==0:
            print(0)
        else:
            while a%k!=0:
                a-=1
                count+=1
        return count
