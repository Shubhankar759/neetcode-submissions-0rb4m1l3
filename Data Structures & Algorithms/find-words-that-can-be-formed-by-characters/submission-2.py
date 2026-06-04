class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count  = Counter(chars)

        res = 0

        for w in words:
            cur_word = Counter(w)
            good = True
            for i in cur_word:
                if cur_word[i] > count[i]:
                    good = False
                    break 
            if good:
                res+=len(w)

        return res
