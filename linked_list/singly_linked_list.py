# create node

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

# creating Linked List
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)

# traverse -> singly linked list
def traverseLL(head):
    curr=head
    while curr is not None:
        print(curr.data, end=" ")

        if curr.next is not None:
            print(" --> ", end=" ")

        curr=curr.next

    print()

traverseLL(head)

# insert at begg
def insertBegg(head, x):
    newNode=Node(x)
    newNode.next=head
    return newNode

newNode = insertBegg(head, 5)
traverseLL(newNode)

# insert at end
def insertatEnd(head, x):
    newNode=Node(x)

    if head is None:
        return newNode

    curr=head

    while curr.next is not None:
        curr=curr.next

    curr.next=newNode

    return head

head = insertatEnd(head, 50)
traverseLL(head)


# insert at pos
def insertPosition(head, x, pos):
    newNode = Node(x)

    # if pos is 0 -> insert at begg
    if pos == 0:
        newNode.next=head
        return newNode

    curr=head

    for i in range(pos-1):
        curr=curr.next

    # change 2 pointers
    newNode.next=curr.next
    curr.next=newNode

    return head

head = insertPosition(head, 75, 2)
traverseLL(head)

# delete begg
def deleteBegg(head):
    if head is None:
        return None

    return head.next

head = deleteBegg(head)
traverseLL(head)

# delete end
def deleteEnd(head):

    if head is None:
        return None

    if head.next is None:
        return None

    curr = head

    while curr.next.next is not None:
        curr= curr.next

    curr.next=None

    return head

head = deleteEnd(head)
traverseLL(head)

# searchLL
def searchLL(head, data):
    curr=head

    while curr is not None:
        if curr.data == data:
            return True
        curr=curr.next

    return False

is_data_found=searchLL(head, 50)
print(is_data_found)

# updateLL
def updateLL(head, old, new):
    curr=head

    while curr is not None:
        if curr.data == old:
            curr.data = new
            return head
        curr=curr.next
    return head

updated_ll = updateLL(head, 75, 750)
traverseLL(updated_ll)

# reverseLL
def reverse(head):
    prev=None
    curr=head

    while curr is not None:
        next_node = curr.next
        curr.next = prev

        prev = curr
        curr=next_node

    return prev

head = reverse(head)
traverseLL(head)

