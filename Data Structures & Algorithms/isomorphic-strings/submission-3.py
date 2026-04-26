class Solution:

    def helper(self,s,t):
        store = dict()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in store:
                if store[s[i]] != t[i]:
                    return False

            else:
                store[s[i]] =  t[i]

        return True

    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.helper(s,t) and self.helper(t,s)

