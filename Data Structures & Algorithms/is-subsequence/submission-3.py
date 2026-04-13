class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        arr = list(t)
        arr_1 = list(s)
        temp =0
        if s=="": return True
        for i in arr:
            if i==arr_1[temp]:
                temp+=1
            
            if temp >= len(arr_1):return True

        if temp >= len(arr_1):
            return True
        else: return False
        