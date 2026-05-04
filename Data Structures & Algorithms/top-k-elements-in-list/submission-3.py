class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        all_nums =  list(set(nums))
        max_val = float('-inf')
        res =[]
        while k:
            max_count = float('-inf')
            best_num = None
            for i in all_nums:
                current_count = nums.count(i)
                if max_count < current_count:
                    max_count = current_count
                    best_num = i
            
            res.append(best_num)
            all_nums.remove(best_num)
            k-=1

        return res