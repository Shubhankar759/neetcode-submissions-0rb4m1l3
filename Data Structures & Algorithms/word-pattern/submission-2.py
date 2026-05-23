class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        checker = dict()
        s = s.split(" ")
        pattern_list = list(pattern)
        
        if len(pattern_list) != len(s): return False
        for i in range(len(pattern_list)):
            if pattern_list[i] in checker:
                if  checker[pattern_list[i]] != s[i]:
                    return False

            else:
                if s[i] in checker.values():
                    return False
                checker[pattern_list[i]] = s[i]

        
        return True