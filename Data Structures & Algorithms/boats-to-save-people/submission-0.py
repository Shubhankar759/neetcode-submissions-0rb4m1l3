class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        res = 0
        i,j = 0,len(people)-1
        people.sort()
        while i <= j:

            total = people[i] + people[j]

            if total > limit:
                j-=1
                res+=1
            else:
                j-=1
                i+=1
                res+=1
            

        return res
            

        