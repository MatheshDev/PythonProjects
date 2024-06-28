class Solution:
    def listSum(self, numList : list[int]) -> int:
        sum = 0
        for n in numList:
            sum += n
        return sum
    
numList = [2,3,6,9]
solution = Solution()
print(solution.listSum(numList))

