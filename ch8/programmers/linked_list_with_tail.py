class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
            curr = curr.next
        return s

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False
        if pos == 1:
            newNode.next = self.head
            self.head = newNode
        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode
        self.nodeCount += 1
        return True

    def getLength(self):
        return self.nodeCount

    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result

    def concat(self, L):
        self.tail.next = L.head
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount

    def popAt(self, pos):
        """ pos 가 가리키는 위치의 (1<= pos <= nodeCount) node를 삭제하고 node의 데이터를 리턴"""
        # 삭제하려는 node가 맨 앞의 것일 때 (pos == 1) - OK
        # - prev 없음
        # -
        # 리스트의 맨 끝의 node를 삭제할 때
        # - tail 조정 필요
        # 빈 리스트라면?
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        if self.head is None:
            raise IndexError

        prev = self.head
        ptr = self.head
        if pos == 1:
            prev = ptr.next  # None
            self.head = prev
            if self.nodeCount == 1:
                self.tail = None

        else:
            for _ in range(1, pos):
                prev = ptr
                ptr = ptr.next
            prev.next = ptr.next
            if pos == self.nodeCount:
                self.tail = prev

        self.nodeCount -= 1
        return ptr.data
