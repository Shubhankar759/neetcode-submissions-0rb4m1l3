class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        i = 0
        counter = tickets[k]
        while counter > 0:
            i = i%len(tickets)
            if tickets[i] == 0:
                i+=1
                continue
            
            res+=1
            tickets[i] -= 1

            if i == k:
                counter -=1
            
            i+=1
        
        
        


        return res
            

        