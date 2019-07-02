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

    currentNode = None
    nextNode = None
    if self.root != None:
      currentNode = self.list[self.root]
      nextNode = currentNode['next']
    currentKey = self.root
    count = 0

    while nextNode != None and count != index:
      count += 1
      currentNode = self.list[nextNode]
      nextNode = currentNode['next']
      currentKey = nextNode

    if count == index and currentNode != None:
      # print('get found! index', index, currentNode['value'])
      return currentNode['value']

    print('get NOT found')
    return -1

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
      # print(self.list)
      return

    node['next'] = self.root
    self.list[self.countKey] = node
    self.root = self.countKey
    # print('last node', self.list[self.countKey])#

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
      # print(self.list)
      return

    currentNode = self.list[self.root]
    nextNode = currentNode['next']
    currentKey = self.root
    # print('root node', currentNode)
    while nextNode != None:
      currentNode = self.list[nextNode]
      nextNode = currentNode['next']
      currentKey = nextNode
      # print('find', currentNode)

    currentNode['next'] = self.countKey
    self.list[self.countKey] = node
    # print('last node', self.list[self.countKey])

  def addAtIndex(self, index, val):
    """
      Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
      :type index: int
      :type val: int
      :rtype: None
    """
    currentNode = None
    nextNode = None
    prevNode = None
    if self.root != None:
      currentNode = self.list[self.root]
      nextNode = currentNode['next']
    currentKey = self.root
    count = 1

    while nextNode != None and count != index and currentKey != None:
      currentNode = self.list[nextNode]
      nextKey = currentNode['next']
      prevNode = self.list[currentKey]
      currentKey = nextKey
      count += 1
      print('currentKey', currentKey)

    print('>>> count', count, 'index', index, 'prevNode', prevNode)
    if prevNode == None and index == 0:  # add in root
      print('add  at heads')
      self.addAtHead(val)
    elif prevNode != None and nextNode == None:  # add in lastNode
      print('add at last')
      self.addAtTail(val)
    elif count == index and prevNode != None:
      # print('Found!', currentKey)
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
    currentNode = None
    nextNode = None
    if self.root != None:
      currentNode = self.list[self.root]
      if currentNode['next'] != None:
        nextNode = self.list[currentNode['next']]

    currentKey = self.root
    prevNode = None
    count = 0

    while currentNode != None and nextNode != None and count != index:
      prevNode = currentNode
      # print('nextNode', nextNode)
      currentNode = nextNode
      if currentNode['next'] != None:
        nextNode = self.list[currentNode['next']]
      currentKey = prevNode['next']
      count += 1
      # print('currentKey', currentKey)

    # print('>>> count', count, 'index', index, 'prevNode', prevNode)
    if prevNode == None and count == 0 and currentNode != None:  # add in root
      self.root = currentNode['next']
    elif prevNode == None and count + 1 == index:  # add in lastNode
      prevNode['next'] = None
    elif count == index:
      # print('Found!', currentKey)
      prevNode['next'] = currentNode['next']
    else:
      print('Not Found!', index)


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

# ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
# [[],[1],[3],[1,2],[1],[1],[1]]
# print(linkedList.addAtHead(1))
# print(linkedList.addAtTail(3))
# print(linkedList.addAtIndex(1, 2))
# print(linkedList.get(1))
# print(linkedList.deleteAtIndex(1))
# print(linkedList.get(1))

# ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
# [[],[1],[3],[4,2],[1],[-1],[1]]
# print(linkedList.addAtHead(1))
# print(linkedList.addAtTail(3))
# print(linkedList.addAtIndex(4, 2))
# print(linkedList.get(1))
# print(linkedList.deleteAtIndex(-1))
# print(linkedList.get(1))

# ["MyLinkedList","addAtHead","addAtIndex","get","get","get"]
# [[],[1],[1,2],[1],[0],[2]]
# print(linkedList.addAtHead(1))
# print(linkedList.addAtIndex(1, 2))
# print(linkedList.printList())
# print(linkedList.get(1))
# print(linkedList.get(0))
# print(linkedList.get(2))

["MyLinkedList", "get", "addAtIndex", "get", "get", "addAtIndex", "get", "get"]
[[], [0], [1, 2], [0], [1], [0, 1], [0], [1]]
print('>>>', linkedList.get(0))
print('>>>', linkedList.addAtIndex(1, 2))
print('>>>', linkedList.get(0))
# print(linkedList.get())
# print(linkedList.addAtIndex())
# print(linkedList.get())
# print(linkedList.get())

# print(linkedList.())
