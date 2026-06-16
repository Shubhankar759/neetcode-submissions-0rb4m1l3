class Solution:
    def firstUniqChar(self, s: str) -> int:
        word_count = Counter(s)
        word = ''
        for i in word_count:
            if word_count[i] == 1:
                word = i
                break

        if word == '': return -1

        return s.index(word)

            
           



        