class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        
        base = sum(c for c, g in zip(customers, grumpy) if g == 0)

        
        extra = sum(c * g for c, g in zip(customers[:minutes], grumpy[:minutes]))
        max_extra = extra

        
        for i in range(minutes, len(grumpy)):
            extra += customers[i] * grumpy[i]           
            extra -= customers[i - minutes] * grumpy[i - minutes]  
            max_extra = max(max_extra, extra)

        return base + max_extra