class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        cnt = Counter(words[0])

        for i in words:
            counting_var = Counter(i)
            for j in cnt:
                cnt[j] = min(cnt[j],counting_var[j])

        res = []

        for i in cnt:
            for j in range(cnt[i]):
                res.append(i)

        return res
