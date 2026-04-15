class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0 
        for i in range(0,len(s)-1):
            temp1 = ord(s[i])
            temp2 = ord(s[i+1])

            sum += abs(temp1-temp2)

        return sum

        