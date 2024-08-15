#3146. Permutation Difference between Two Strings

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        dic_s={}
        dic_t={}
        res=0
        for i in range(len(s)):
            dic_s[s[i]]=i
        for i in range(len(t)):
            dic_t[t[i]]=i
        for i in s:
            res+= abs(dic_s[i]-dic_t[i])
        return res