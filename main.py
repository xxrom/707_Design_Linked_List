class MyLinkedList(object):

    def __init__(self):
        self.list = []
        self.root = None
        self.countKey = 0

    def initNode(self, value, next=None):
        self.countKey += 1
        return {value, next}

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        if self.root == None:
            {
                node = self.initNode(val, self.countKey)
                self.root = self.countKey
                self.list.push(node)
                print(self.list)
            } else {

            }

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get(index)
obj.addAtHead(123)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


# linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
# linkedList.get(1);            // returns 2
# linkedList.deleteAtIndex(1);  // now the linked list is 1->3
# linkedList.get(1);            // returns 3
