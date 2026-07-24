import math
class Solution:
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)

        def can_finish(speed):
            total_hours = sum((p+speed-1) // speed for p in piles)
            return total_hours <= h
        res = right
        while left <= right:
            mid = (left + right) // 2
            if can_finish(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1 
        return res
        
        