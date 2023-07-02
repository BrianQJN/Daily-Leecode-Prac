"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.


Example:
Input: piles = [3,6,7,11], h = 8
Output: 4
"""
import math
class Solution(object):
    def kokoEatingBananas(self, piles, h):
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            mid = (l + r) // 2

            totalTime = 0

            for p in piles:
                totalTime += math.ceil(p/mid)
            
            if totalTime > h:
                l = mid + 1
            else:
                r = mid - 1
                res = min(res, mid)
        
        return res
    

if __name__ == '__main__':
    test = Solution
    print(test.kokoEatingBananas(test, [3,6,7,11], h = 8))