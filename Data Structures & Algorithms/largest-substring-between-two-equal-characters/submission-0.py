class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:

        n = len(s)
        res = -1

        for i in range(0,n):
            for j in range(i+1,n):

                if s[i] == s[j] and j-i > res:
                    res = j-i - 1


        return res


        