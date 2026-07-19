class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        

        counter = 0
        for i in range(k):
            if blocks[i] == 'W':
                counter+=1

    

        mini = counter
        for i in range(k,len(blocks)):

            if blocks[i - k] == 'W':
                counter -= 1

            if blocks[i] == 'W':
                counter += 1
            

            
            mini = min(mini,counter)
            
        
        return mini 


                
