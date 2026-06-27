import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        
        j = -1
        for i in range(len(clean_text)//2):
            # if not s[i].isalnum():
            #     i+=1
            #     continue
            # if not s[j].isalnum():
            #     j-=1
            #     continue

            if clean_text[j] == clean_text[i]:
                i+=1
                j-=1
            else:
                return False

        return True
