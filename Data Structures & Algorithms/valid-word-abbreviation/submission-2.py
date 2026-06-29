class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        n, j = len(word), 0
        i = 0
        m = len(abbr)

        while i < m:
            if abbr[i].isalpha():
                if j >= n or word[j] != abbr[i]:
                    return False
                j += 1
                i += 1
            else:
                if abbr[i] == '0':  # leading zero not allowed
                    return False
                num = 0
                while i < m and abbr[i].isdigit():
                    num = num * 10 + int(abbr[i])
                    i += 1
                j += num  # apply the jump ONCE, after parsing full number

        return j == n




            

            



        