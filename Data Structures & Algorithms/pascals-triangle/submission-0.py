class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows ==1:
            return [[1]]
        triangle = [[1],[1,1]]
        if numRows ==2:
            return triangle

        
        for i in range(3,numRows+1):
            last_list = triangle[-1]
            temp=[1,1]
            for x in range(1,i-1):
                temp.insert(-1,last_list[x]+last_list[x-1])
            
            triangle.append(temp)

        return triangle





        