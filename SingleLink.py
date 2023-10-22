class Node:
    def __init__ (self, data, next=None):
        self.data = data        # Value if the node
        self.next = next        # Property of the next node

class SingleLinkedList:
    def __init__(self):         ## Head is a property that points to the first node in the list
        self.head = None        ## Initially the linked list is empty

    def printList(self):
        if self.head is None:
            print("The linked list is empty")
        else:
            temp = self.head            ## You dont want to change where the head is point so made a temp var ##
            while (temp): 
                print (temp.data, " --> ", end = "")  ## Get data from current node ##
                temp = temp.next                      ## Go to next node ## 
            print("None")

    # inserting element/node at the front/beginning/head
    def insert_begin(self, data):
        new_node = Node(data)               ## 1. Created new node
        new_node.next = self.head           ## 2. Point the new node.next to the current head/ beginning
        self.head = new_node                ## 3. Update the to the new head since the new node is now 
                                            ##    at the beginning of our list it is out new head

    # inserting element/node at the last/end/tail
    def insert_end(self, data):
        new_node = Node(data)
        if(self.head is None):
            self.head = new_node
        else:
            temp = self.head                ## You dont want to change where the head is point so made a temp var ##
            while(temp.next):               ## Travel to the last/null node where .next should point to null/not exist
                temp = temp.next            ## Tells is to keep going is temp.next exists
            temp.next = new_node            ## Change the .next to point to your new node

    # inserting a node at a specified index
    def insert_after(self, data, pos):
       
        new_node = Node(data)
        
        if(self.head is None):
            self.head = new_node
        else:
            count = 1
            temp = self.head
            while(temp.next is not None and count < pos):
                temp = temp.next
                count += 1
          
            new_node.next = temp.next
            temp.next = new_node
            
    def insert_before(self, data, pos):
        new_node = Node(data)
        
        if(self.head is None):
             self.head = new_node
        else:
            pass