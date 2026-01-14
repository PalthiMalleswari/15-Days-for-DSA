# Problem - https://leetcode.com/problems/min-stack/description/

class MinStack:

    def __init__(self):
        
        self.stack1 = []
        self.stack2 = []

    def push(self, val: int) -> None:

        if not self.stack2 or self.stack2[-1]>=val:
            self.stack2.append(val)
        self.stack1.append(val)
        
    def pop(self) -> None:
        
        if self.stack1 and self.stack2:
            if self.stack1[-1] == self.stack2[-1]:
                self.stack1.pop()
                self.stack2.pop()
            else:
                self.stack1.pop()
        

    def top(self) -> int:
        return self.stack1[-1]
        

    def getMin(self) -> int:
        return self.stack2[-1]
        

Time Complexity - O(1) for all operations
Space Complexity - O(2N) for both stacks
                     
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
