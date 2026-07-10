class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for l in range(n - 1, i + 2, -1):
                
                if l < n - 1 and nums[l] == nums[l + 1]:
                    continue

                j, k = i + 1, l - 1  

                while j < k:
                    total = nums[i] + nums[j] + nums[k] + nums[l]

                    if total < target:
                        j += 1
                    elif total > target:
                        k -= 1
                    else:
                        res.append([nums[i], nums[j], nums[k], nums[l]])

                       
                        while j < k and nums[j] == nums[j + 1]:
                            j += 1
                        while j < k and nums[k] == nums[k - 1]:
                            k -= 1

                        j += 1
                        k -= 1

        return res
        