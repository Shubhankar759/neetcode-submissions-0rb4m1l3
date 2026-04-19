class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        total,temp=0,0
        for i in nums:
            if i ==0:
                total=0

            total+=i

            if temp<total:temp=total

        return temp