class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        wordin = {
            'b':0,
            'a':0,
            'l':0,
            'o':0,
            'n':0,

        }

        for i in text:
            if i in 'balloon':
                wordin[i] += 1

        final_count = []
        final_count.append(wordin['b']/1)
        final_count.append(wordin['a']/1)
        final_count.append(wordin['l']/2)
        final_count.append(wordin['o']/2)
        final_count.append(wordin['n']/1)

        

        return int(min(final_count))
