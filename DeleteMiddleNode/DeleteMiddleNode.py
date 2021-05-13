'''
Cracking the coding interview
Chapter 2 - Linked List pg 94
Linked List - Delete Middle Node
----------------------------------------
Question: Delete Middle Node - Implement an algorithm to delete a node in the middle (i.e. any node by the first and last node, no necessaruky the exact middle)
of a singly linked list, given only acess to that node.
Example: 
input: The node c from the linked list a-> b-> c-> d-> e-> f
output: nothing is returned but the new linked list is a->b->d->e->f (c is removed)
Constraits or Questions you need to ask:
- Try brute force method. 
- Get the linked list legth

Solution notes:
Case 1: only 1 element in the linked list, do nothing
Case 2: only 2 elements in linked list, do nothing
Case 3: odd number length in linked list, delete middle node
Case 4: Even number length in lnked list but > 2, delete length / 2 node
'''
import math

#Node class
class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

#Wrapper class
class linked_list:
    def __init__(self):
        self.head = node()

    #Add a node to the end of a linked list
    def append(self,data):
        new_node = node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    #Return the Length of the linked list
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    #Print the linked list
    def display(self):
        elements = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elements.append(cur.data)
        print(elements)

    def deleteMiddleNode(self):
        #Get list length 
        listLength = self.length()
        #If list length is 0, 1, or 2 return error and exit
        if listLength == 0 or listLength == 1 or listLength == 2:
            print("Length is not computable to remove middle node ")
            return
        #if list length is even and > 2
        if listLength > 2 and listLength % 2 == 0:
            #Index to remove is length / 2
            index = (listLength / 2) - 1
            
            cur = self.head
            indexCounter = 0
            while True:
                lastNode = cur
                cur = cur.next
                if(indexCounter == index):
                    lastNode.next = cur.next
                    return
                indexCounter += 1

        #If list length is odd
        if listLength % 2 == 1:
            #Getting the index that needs to be removed 
            index = (listLength/2) - .5
           

            cur = self.head
            counterIndex = 0
            while True:
                lastNode = cur
                cur = cur.next
                if(counterIndex == index):
                    lastNode.next = cur.next
                    return
                counterIndex += 1







myList = linked_list()
#While list is empty
#myList.display()

#Adding elements to linked list
myList.append(2)
myList.append(1)
myList.append(6)
myList.append(8)
myList.append(5)
#Remove middle
myList.deleteMiddleNode()

#Display current linked list
myList.display()
