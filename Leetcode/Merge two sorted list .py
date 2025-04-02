# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node to help simplify the merge process
        dummy = ListNode()
        current = dummy
        
        # Traverse both lists and merge them
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next  # Move the current pointer
        
        # If there are any remaining nodes in either list, append them
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        # The merged list starts from dummy.next
        return dummy.next

# Helper function to create a new node
def createNode(val):
    return ListNode(val)

# Helper function to print the linked list
def printList(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

# Example usage
if __name__ == "__main__":
    # Create two sorted lists
    list1 = createNode(1)
    list1.next = createNode(2)
    list1.next.next = createNode(4)

    list2 = createNode(1)
    list2.next = createNode(3)
    list2.next.next = createNode(4)

    # Merge the two lists
    solution = Solution()
    mergedList = solution.mergeTwoLists(list1, list2)
    
    # Print the merged list
    print("Merged List: ", end="")
    printList(mergedList)  # Output: 1 1 2 3 4 4
