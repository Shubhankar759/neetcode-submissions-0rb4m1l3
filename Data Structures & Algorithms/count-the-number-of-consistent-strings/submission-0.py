class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = Counter(allowed)
        res = 0
        for i in words:
            tempcount = Counter(i)
            good = True

            for j in tempcount:
                if count[j] <= 0:
                    good = False
            
            if good:
                res +=1

        
        return res

        