class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      
        arr = set(s).symmetric_difference(set(t))
        if len(arr) > 0:
            return False
        else: arr = list(set(t))
        for i in arr:
            if list(s).count(i) == list(t).count(i):
                continue
            else:
                return False

        return True