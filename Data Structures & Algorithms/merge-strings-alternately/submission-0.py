class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n=0
        word1_largest = bool()
        if len(word1) > len(word2):
            n = len(word2)
            word1_largest = True
        else:
            n= len(word1)
            word1_largest = False

        res = ''
        for i in range(n):

            res += word1[i]
            res += word2[i]


        if  word1_largest:
            res += word1[n:]
        else:
            res += word2[n:]


        return res

            
            

        