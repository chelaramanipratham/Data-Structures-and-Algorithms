class Solution:

    def possibleWords(self,a,N):
        #Your code here
        keypad = {
            2 : ["a", "b", "c"],
            3 : ["d", "e", "f"],
            4 : ["g", "h", "i"],
            5 : ["j", "k", "l"],
            6 : ["m", "n", "o"],
            7 : ["p", "q", "r", "s"],
            8 : ["t", "u", "v"],
            9 : ["w", "x", "y", "z"]
        }

        ans = []

        def helper(idx, cur):
            if len(cur) == N:
                ans.append(cur)
                return
            for val in keypad[a[idx]]:
                helper(idx+1, cur + val)

        helper(0, "")
        return ans