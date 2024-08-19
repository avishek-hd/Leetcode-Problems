#2652. Sum Multiples
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        i=1
        res=0
        while(i<=n):
            if i%3==0 or i%5==0 or i%7==0:
                res+=i
            i+=1
        return res