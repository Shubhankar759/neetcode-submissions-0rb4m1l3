class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        counter =0

        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                counter+=1
            elif nums[i-1] > nums[i] :
                counter-=1
            elif nums[i-1] == nums[i]:
                if counter >=0:
                    counter +=1
                else:
                    counter-=1

        
        if abs(counter) == (len(nums)-1):
            return True
        else:
            return False
