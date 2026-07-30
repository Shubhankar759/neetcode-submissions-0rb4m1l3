class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:


        
        sum_of  =0
        n = len(nums)
        
        for i in range(n):
            curSum = 0
            for j in range(i,n):
                curSum+=nums[j]
                if curSum == goal:
                    sum_of+=1

        return sum_of