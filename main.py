class Node(object):

    def __init__(self, data):
        self.data = data
        self.nextNode = None  # NULL ? =)


class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if self.size < index or index < 0:
            return -1

        count = 0
        currentNode = self.head
        previousNode = None
        while count != index and currentNode is not None:
            previousNode = currentNode
            currentNode = currentNode.nextNode
            count += 1

        if currentNode is not None:
            return currentNode.data
        else:
            return -1

    # inserHead - добаление блока в начало листа
    # data - number, данные для хранения
    def addAtHead(self, data):
        self.size = self.size + 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode  # если список пуст то [N] -> NULL
        else:
            newNode.nextNode = self.head  # если не пуст
            self.head = newNode  # [N] -> [H] -> NULL

    def deleteAtIndex(self, index):
        if self.head is None or self.size < index:
            return -1

        self.size = self.size - 1

        count = 0
        currentNode = self.head
        previousNode = None
        while count != index and currentNode is not None:
            previousNode = currentNode
            currentNode = currentNode.nextNode
            count += 1

        if previousNode is None:  # если сразу нашли элемент первый
            self.head = currentNode.nextNode
        elif currentNode is not None:  # если не первый элемент нашли
            previousNode.nextNode = currentNode.nextNode
        else:
            self.size = self.size + 1

    def addAtIndex(self, index, data):
        if self.size < index:
            return -1
        if self.size == index or index < 0:
            return self.addAtTail(data)

        self.size = self.size + 1

        count = 0
        currentNode = self.head
        previousNode = None
        while count != index and currentNode is not None:
            previousNode = currentNode
            currentNode = currentNode.nextNode
            count += 1

        if previousNode is None:  # если сразу нашли элемент первый
            self.addAtHead(data)
            print('add at Head!')
        elif currentNode is not None:  # если не первый элемент нашли
            newNode = Node(data)
            previousNode.nextNode = newNode
            newNode.nextNode = currentNode

            # previousNode.nextNode = currentNode.nextNode
        else:
            self.size = self.size - 1

    # O(1)
    def size1(self):
        return self.size

    # O(N) not so good !!!
    def size2(self):
        actualNode = self.head
        size = 0

        while actualNode is not None:
            size += 1
            actualNode = actualNode.nextNode

        return size

    # O(N)
    def addAtTail(self, data):
        self.size += 1
        newNode = Node(data)

        if self.head is None:
            return self.addAtHead(data)

        lastNode = self.head  # доходим до последнего элемента перед NULL
        while lastNode.nextNode is not None:
            lastNode = lastNode.nextNode

        lastNode.nextNode = newNode  # переприсваиваем nextNode на newNode

    # O(N)
    def traverseList(self):  # выводит весь список
        actualNode = self.head

        while actualNode is not None:
            print("%d " % actualNode.data, end='')
            actualNode = actualNode.nextNode
        print('')


linkedList = MyLinkedList()


print(linkedList.get(0))
linkedList.addAtIndex(0, 1)
linkedList.traverseList()

# linkedList.addAtHead(12)
# linkedList.addAtHead(122)
# linkedList.addAtHead(3)
# linkedList.addAtTail(31)
# linkedList.traverseList()

# TEST get
# print(linkedList.get(-1))
# print(linkedList.get(0))
# print(linkedList.get(1))
# print(linkedList.get(2))
# print(linkedList.get(3))

# TEST add At Index
# linkedList.addAtIndex(5, 77)
# linkedList.traverseList()
# linkedList.addAtIndex(-1, 88)
# linkedList.traverseList()
# linkedList.addAtIndex(100, 99)
# linkedList.traverseList()

# TEST Del
# linkedList.deleteAtIndex(0)
# linkedList.traverseList()

# linkedList.deleteAtIndex(1)
# linkedList.traverseList()

# linkedList.deleteAtIndex(0)
# linkedList.traverseList()


# linkedList.deleteAtIndex(1)
# linkedList.traverseList()
print("size1 %i " % linkedList.size1())
# linkedList.deleteAtIndex(0)
# linkedList.traverseList()
# print("size1 %i " % linkedList.size1())

# linkedList.traverseList()
# print("size1 %i " % linkedList.size1())
# print("size2 %d " % linkedList.size2())
