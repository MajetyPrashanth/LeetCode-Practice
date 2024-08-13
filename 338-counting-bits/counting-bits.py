class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[i for i in range(0,n+1)]
        ans=[bin(i).count('1') for i in l]
        return ans