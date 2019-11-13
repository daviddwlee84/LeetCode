# Two Pointer

## Usage

### Find middle element in a linked list

```py
def findMiddle(self, head):

    # The pointer used to disconnect the left half from the mid node.
    slowPtr = head
    fastPtr = head

    # Iterate until fastPr doesn't reach the end of the linked list.
    while fastPtr and fastPtr.next:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next

    return slowPtr # this will be the middle element
```

* Time Complexity: $O(N/2)$

We can do a time-space tradeoff that convert linked list into a list then we can get the middle element with $O(1)$

## Resources

* [Two Pointers Technique - GeeksforGeeks](https://www.geeksforgeeks.org/two-pointers-technique/)
