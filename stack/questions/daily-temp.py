# Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days
# you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be 
# [1, 1, 4, 2, 1, 1, 0, 0].

# Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range 
# [30, 100].

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        st = []
        ans = [0 for i in T]
        si = len(T)
        for i in range(len(T)-1):
            cur = T[i]
            nex = T[i + 1]
            if(nex > cur):
                ans[i] = 1
                while(len(st) != 0):
                    if(T[st[len(st)-1]] < nex):
                        ind = st.pop()
                        ans[ind] = i - ind + 1
                    else:
                        break
            else:
                st.append(i)
        return ans