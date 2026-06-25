class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        res = []
        vowels = ['a','e','i','o','u']
        for i in queries:
            counter = 0
            var_str = words[i[0]:i[1]+1]
            for j in var_str:
                if j[0] in vowels and j[-1] in vowels:
                    counter += 1
            

            res.append(counter)


        return res
            
        