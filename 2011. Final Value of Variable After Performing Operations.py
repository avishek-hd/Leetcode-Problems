
#2011. Final Value of Variable After Performing Operations

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        dict={"--X":-1,"X--":-1, "X++":1, "++X":1}
        sum=0
        for i in operations:
            sum+= dict[i]
        return sum