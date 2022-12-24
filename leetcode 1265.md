we got two APIs printValue() print current node's value and getNext() get next node

def a function to print a linklist in reverse:

```
class Solution:
    def printLinkedListInReverse(self, head) -> None:
        if head==None:
            return None
        else:
            self.printLinkedListInReverse(head.getNext())
            head.printValue()
 ```           
![image](https://user-images.githubusercontent.com/111692657/209423132-2d38c6ab-c191-4dd9-b2fd-405c333020f6.png)
