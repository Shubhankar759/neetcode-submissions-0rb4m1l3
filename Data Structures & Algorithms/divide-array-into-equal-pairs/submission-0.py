class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums)%2 != 0: return False

        counter = defaultdict(int)

        for i in nums:
            counter[i] += 1

        for i in counter:
            if counter[i]%2!=0:
                return False
            

        return True