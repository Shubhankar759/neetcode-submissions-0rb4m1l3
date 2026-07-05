class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()
        counter = 0
        j = 0
        if len(s) == 0: return 0
        for i in range(len(s)):
            if g[j] <= s[i]:
                j+=1
                counter+=1

            if j == len(g):
                break


        return counter