# Problem - https://leetcode.com/problems/implement-queue-using-stacks/description/
#  Reference - https://leetcode.com/problems/implement-queue-using-stacks/solutions/64206/short-o1-amortized-c-java-ruby-by-stefan-ktm3/
class MyQueue:

    def __init__(self):
        
        self.stack = []

    def push(self, x: int) -> None:
        
        self.stack.append(x)
        

    def pop(self) -> int:

        if self.stack:
            ans = self.stack[0]
            self.stack.remove(ans)
            return ans
        return -1

    def peek(self) -> int:
        if self.stack:
            return self.stack[0]
        
    def empty(self) -> bool:

        return False if self.stack else True
        
