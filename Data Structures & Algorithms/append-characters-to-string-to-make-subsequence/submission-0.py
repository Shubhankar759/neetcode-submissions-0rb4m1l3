class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        pointer_t = 0
        for i in range(0,len(s)):
            if s[i] == t[pointer_t]: pointer_t+=1
            
            if pointer_t == len(t): return 0

        return len(t) - pointer_t

        