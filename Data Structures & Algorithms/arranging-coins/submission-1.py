class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        nums = 1
        coins = 0

        if n == 1 or n ==2:
            return 1
        if n == 3:
            return 2
        

        while coins < n:

            coins += nums
            nums += 1

        return nums  -2