class MyLinkedList(object):

  def __init__(self):
    self.list = {}
    self.root = None
    self.countKey = 0

  def initNode(self, value, next=None):
    self.countKey += 1
    return {"value": value, "next": next}

  def printList(self):
    print('PrintList ', self.list[self.root])
    nextNode = self.list[self.root]['next']
    while nextNode != None:
      print('printList ', self.list[nextNode])
      nextNode = self.list[nextNode]['next']

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
    node = self.initNode(val)
    if self.root == None:
      self.root = self.countKey
      self.list[self.countKey] = node
      print(self.list)
      return

    currentNode = self.list[self.root]
    node['next'] = self.root
    self.list[self.countKey] = node
    self.root = self.countKey
    print('last node', self.list[self.countKey])

  def addAtTail(self, val):
    """
      Append a node of value val to the last element of the linked list.
      :type val: int
      :rtype: None
    """
    node = self.initNode(val)
    if self.root == None:
      self.root = self.countKey
      self.list[self.countKey] = node
      print(self.list)
      return

    currentNode = self.list[self.root]
    nextNode = currentNode['next']
    currentKey = self.root
    print('root node', currentNode)
    while nextNode != None:
      currentNode = self.list[nextNode]
      nextNode = currentNode['next']
      currentKey = nextNode
      print('find', currentNode)

    currentNode['next'] = self.countKey
    self.list[self.countKey] = node
    print('last node', self.list[self.countKey])

  def addAtIndex(self, index, val):
    """
      Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
      :type index: int
      :type val: int
      :rtype: None
    """
    currentNode = self.list[self.root]
    nextNode = currentNode['next']
    currentKey = self.root
    prevNode = None
    count = 0

    while nextNode != None and count != index:
      currentNode = self.list[nextNode]
      nextKey = currentNode['next']
      prevNode = self.list[currentKey]
      currentKey = nextKey
      count += 1
      print('currentKey', currentKey)

    print('>>> count', count, 'index', index, 'prevNode', prevNode)
    if prevNode == None and count == 0:  # add in root
      self.addAtHead(val)
    elif prevNode == None and count + 1 == index:  # add in lastNode
      self.addAtTail(val)
    elif count == index:
      print('Found!', currentKey)
      node = self.initNode(val)
      node['next'] = prevNode['next']
      prevNode['next'] = self.countKey
      self.list[self.countKey] = node
    else:
      print('Not Found!', index)

  def deleteAtIndex(self, index):
    """
      Delete the index-th node in the linked list, if the index is valid.
      :type index: int
      :rtype: None
    """


# Your MyLinkedList object will be instantiated and called as such:
linkedList = MyLinkedList()
# param_1 = obj.get(index)
# linkedList.addAtTail(1213)
# linkedList.addAtHead(1011)
# linkedList.addAtHead(789)
# linkedList.addAtHead(456)
# linkedList.addAtHead(123)
# linkedList.addAtTail(1415)
# linkedList.addAtIndex(6, 131400)
# linkedList.addAtIndex(0, 1)
# linkedList.printList()

linkedList.addAtHead(1)
linkedList.addAtTail(3)
linkedList.addAtIndex(1, 2)
linkedList.addAtIndex(3, 4)
linkedList.addAtTail(5)
linkedList.addAtHead(0)
linkedList.printList()

# linkedList.addAtTail(val)
# linkedList.addAtIndex(index,val)
# linkedList.deleteAtIndex(index)

# linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
# linkedList.get(1);            // returns 2
# linkedList.deleteAtIndex(1);  // now the linked list is 1->3
# linkedList.get(1);            // returns 3
