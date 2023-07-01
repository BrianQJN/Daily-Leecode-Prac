"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] 
is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for 
which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
"""
class Solution(object):
    def dailyTemperatures(self, temperatures):
        i = 0
        res = []

        for temp in temperatures:
            j = 0
            for temp2 in temperatures[i+1:]:
                if temp2 > temp:
                    res.append(j+1)
                    break
                else:
                    j += 1
            if j == len(temperatures[i+1:]):
                res.append(0)
            
            i += 1

        return res
    
    def dailyTemperatures2(self, temperatures):
        stack = []
        res = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI] = index - stackI
            stack.append((temp, index))
        
        return res


if __name__ == "__main__":
    test = Solution
    print(test.dailyTemperatures(test,[73,74,75,71,69,72,76,73]))
    print(test.dailyTemperatures2(test,[73,74,75,71,69,72,76,73]))