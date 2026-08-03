class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        stack = []

        for i in logs:

            

            if i == '../':
                if len(stack) == 0: continue
                x = stack.pop()
            elif i == "./":
                pass
            else:
                stack.append(i)

        
        return len(stack)