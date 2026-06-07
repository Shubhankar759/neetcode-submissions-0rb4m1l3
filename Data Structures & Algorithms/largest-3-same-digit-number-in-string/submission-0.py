class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max = -1
        num = list(map(lambda x: int(x), num))
        for i in range(0,len(num)):
            if i+1 > len(num) or i+2 > len(num)-1: break
            if num[i] > max and num[i+1] == num[i+2] and num[i] == num[i+2]:
                max = num[i]
        if max == -1 : return ""
        res = str(max)*3
        return res
            




        