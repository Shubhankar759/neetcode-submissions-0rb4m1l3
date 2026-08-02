from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_d = deque()  # decreasing — front is max
        min_d = deque()  # increasing — front is min
        
        l = 0
        res = 0

        for r in range(len(nums)):
            # Maintain decreasing deque for max
            while max_d and nums[max_d[-1]] <= nums[r]:
                max_d.pop()
            max_d.append(r)

            # Maintain increasing deque for min
            while min_d and nums[min_d[-1]] >= nums[r]:
                min_d.pop()
            min_d.append(r)

            # Shrink window if condition violated
            while nums[max_d[0]] - nums[min_d[0]] > limit:
                l += 1
                if max_d[0] < l:
                    max_d.popleft()
                if min_d[0] < l:
                    min_d.popleft()

            res = max(res, r - l + 1)

        return res