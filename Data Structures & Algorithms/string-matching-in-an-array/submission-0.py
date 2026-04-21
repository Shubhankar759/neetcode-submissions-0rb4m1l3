class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        output = []
        for i in words:
            for j in words:
                if i == j: continue
                if j.find(i) != -1: output.append(i)

        return list(set(output))
                
        