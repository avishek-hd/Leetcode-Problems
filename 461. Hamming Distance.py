#461. Hamming Distance
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor= x^y
        c=0
        for i in range(32):
            if(xor>>i)&1==1:
                c+=1
        return c