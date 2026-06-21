class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        res = len(sandwiches)
        fq = Counter(students)

        for sandwich in sandwiches:

            if fq[sandwich] > 0 :
                res -=1 
                fq[sandwich] -=1

            else:
                break
        
        return res
