class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp =0
        for i in range(0,len(nums)):
            if val != nums[i]:
                nums[temp] = nums[i]
                temp+=1

                
        return temp