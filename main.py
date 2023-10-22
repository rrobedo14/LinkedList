from SingleLink import SingleLinkedList

llist = SingleLinkedList()

llist.insert_begin(3)
llist.printList()
llist.insert_begin(4)
llist.printList()
llist.insert_begin(5)
llist.printList()

llist.insert_end(2)
llist.printList()
llist.insert_end(1)
llist.printList()
llist.insert_end(0)
llist.printList()

llist.insert_after('a', 2)
llist.printList()
llist.insert_after('b', 0)
llist.printList()
llist.insert_after('c', 20)
llist.printList()
