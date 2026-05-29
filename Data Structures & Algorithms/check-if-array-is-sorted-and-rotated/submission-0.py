class Solution:
    def check(self, nums: List[int]) -> bool:
        counter = 0

        for i in range(1,len(nums)):
            if nums[i - 1] > nums[i]:
                counter +=1
                if counter > 1:
                    return False
            

        if nums[-1] > nums[0]:
            counter  +=1  
        return bool(counter<=1)
