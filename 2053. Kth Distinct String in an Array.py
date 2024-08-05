from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        word_count=Counter(arr)
        for word in arr:
            if word_count[word]==1:
                k-=1
            if k==0:
                return word
        return ""
            