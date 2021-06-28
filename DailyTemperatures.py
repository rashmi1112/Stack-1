# TC: O(N) Amortized, Actual TC: O(2N) since we are iterating over the entire array and in worst case, there can be N elements in the stack unresolved. 
#     Resolving them would take another operation of N time.
# SC: O(N) since we are using a stack to store the unresolved elements.

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures or len(temperatures) == 0: 
            return 
        
        n = len(temperatures)
        result = [0]*n
        stack = []
        
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack[-1]
                result[idx] = i - idx
                stack.pop()
            stack.append(i)
        
        return result
