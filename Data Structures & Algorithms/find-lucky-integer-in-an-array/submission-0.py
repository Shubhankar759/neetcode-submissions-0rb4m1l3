class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = defaultdict(int)
        res = -1
        for i in arr:
            counter[i] += 1
        
        for key, value in counter.items():
            if key == value and res<= value:
                res = value
        
        return res
                

        