# Time Complexity : O(2^N)  # Explore all possibilities with pruning
# Space Complexity : O(2^N) # Store valid expressions
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Explanation:
# First compute minimum number of invalid left and right parentheses.
# Use backtracking to remove them while maintaining valid structure.
# Only expressions with balanced parentheses are added to results.

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = set()
        
        left = right = 0
        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if left == 0:
                    right += 1
                else:
                    left -= 1
        
        def backtrack(i, l, r, open_p, path):
            if i == len(s):
                if l==0 and r==0 and open_p==0:
                    res.add(path)
                return
            
            ch = s[i]
            
            if ch == '(' and l > 0:
                backtrack(i+1, l-1, r, open_p, path)
            
            if ch == ')' and r > 0:
                backtrack(i+1, l, r-1, open_p, path)
            
            if ch not in '()':
                backtrack(i+1, l, r, open_p, path+ch)
            elif ch == '(':
                backtrack(i+1, l, r, open_p+1, path+ch)
            elif ch == ')' and open_p > 0:
                backtrack(i+1, l, r, open_p-1, path+ch)
        
        backtrack(0, left, right, 0, "")
        return list(res)