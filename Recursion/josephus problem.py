class Solution:
    def josephus(self,n,k):
        if(n ==1):
            return n

        return (self.josephus(n-1,k)+k-1)%n+1
        #Your code here