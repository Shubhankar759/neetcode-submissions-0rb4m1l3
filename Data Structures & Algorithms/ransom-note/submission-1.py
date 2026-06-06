class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_1 = Counter(ransomNote)
        count_2 = Counter(magazine)

        for i in count_1:
            if count_1[i] > count_2[i]:
                return False

        return True