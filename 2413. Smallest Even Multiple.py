
#2413. Smallest Even Multiple

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        m=1
        i=n
        while(i>=n):
            if(i%2==0):
                return i
            m+=1
            i=i*m
