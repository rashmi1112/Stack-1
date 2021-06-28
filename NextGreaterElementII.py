# TC: Asymptotic: O(N) and Actual = O(3N) since we will be iterating over the array twice since it is circular. And in worst case, to pop all elements from stack would take O(N) time.
# SC: O(N) since in the worst case, the stack would be filled with N items.

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 0: 
            return
        
        n = len(nums)
        result = [-1]*n
        stack = []
        
        for i in range(2*n): 
            while stack and nums[i % n] > nums[stack[-1]]: 
                idx = stack[-1]
                result[idx] = nums[i % n]
                stack.pop()
            if i < n: 
                stack.append(i)
        
        return result
