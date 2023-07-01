def subsets(nums):
    result = []
    
    def backtrack(start, subset):
        result.append(subset[:])
        
        for i in range(start, len(nums)):
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
    
    backtrack(0, [])
    return result

print(subsets([1,2,3]))


