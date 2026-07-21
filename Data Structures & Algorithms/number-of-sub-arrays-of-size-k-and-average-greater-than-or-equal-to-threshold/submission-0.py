class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        counter = 0
        sum_of = sum(arr[:k-1])

        for L in range(len(arr)-k+1):

            sum_of += arr[L+k-1]

            if (sum_of//k) >= threshold:
                counter+=1
            
            sum_of-= arr[L]
            

        return counter

            

                


         

        
        return counter



        