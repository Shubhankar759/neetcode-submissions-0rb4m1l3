class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        size_of_arr = len(nums)
        res = []
        for i in range(1,size_of_arr+1):
            if i in nums:
                continue
            else:
                res.append(i)

        return res

        