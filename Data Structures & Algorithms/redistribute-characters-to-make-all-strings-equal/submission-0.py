class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        whole_string = ""
        for i in words:
            whole_string += i

        count_of_letter = Counter(whole_string)

        for i in count_of_letter:
            if count_of_letter[i] % len(words) != 0:
                return False

        return True



        
        