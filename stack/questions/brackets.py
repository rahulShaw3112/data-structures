# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false
# Example 4:

# Input: "([)]"
# Output: false
# Example 5:

# Input: "{[]}"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        ob = {'{':'}', '(':')', '[':']'}
        for i in s:
            if(i in ob):
                st.append(i)
            else:
                if(len(st) != 0):
                    t = st.pop()
                    if(ob[t] != i):
                        return False
                else:
                    return False
        if(len(st) == 0):
            return True  
        else: 
            return False
                