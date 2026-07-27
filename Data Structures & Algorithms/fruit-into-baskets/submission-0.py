class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        res = 0 

        for i in range(n):
            types = set()
            pointer = i
            while pointer < n and (len(types) < 2 or fruits[pointer] in types):
                types.add(fruits[pointer])
                pointer +=1

            res = max(pointer-i,res)

        return res
            




        