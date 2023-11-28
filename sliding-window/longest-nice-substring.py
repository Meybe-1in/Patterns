class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def helper(st):
            if len(st) <2:
                return ""
            bad_set = set(st) - set(st.swapcase())

            if not bad_set:
                return st
            if len(bad_set) == (ln_st:=len(st)):
                return ""

            start = 0
            res = ""

            for ind, sym in enumerate(st):
                if sym in bad_set:
                    if ind - start > len(res):
                        res = max(res, helper(st[start:ind]), key=len)
                    start = ind+1

            if ln_st - start-1 > len(res):
                res = max(res, helper(st[start:]), key=len)
            return res
        return helper(s)
            