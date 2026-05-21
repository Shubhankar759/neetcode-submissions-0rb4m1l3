class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        size_of_mat = len(grid)
        list_double  = []
        list_all_nums = [i for i in range(1, size_of_mat*size_of_mat + 1)]   
        double = 0
        for i in range(size_of_mat):
            for j in range(size_of_mat):
                
                if grid[i][j] in list_double:
                    double = grid[i][j]

                list_double.append(grid[i][j])

        
        missing = list(set(list_all_nums) -  set(list_double))

        return [double,missing[0]]




