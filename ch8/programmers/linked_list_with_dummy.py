class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail

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
        if pos < 0 or pos > self.nodeCount:
            return None

        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr

    def insertAfter(self, prev, newNode):
        newNode.next = prev.next
        if prev.next is None:
            self.tail = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True

    def insertAt(self, pos, newNode):
        # (1) pos 인덱스 범위 (pos<1, pos>nodeCount+1)
        # (2) pos == 1 일때 : head -> newNode
        # (3) pos == nodeCount+1 일때: tail = prev

        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos != 1 and pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)

        return self.insertAfter(prev, newNode)

    def getLength(self):
        return self.nodeCount

    def traverse(self):
        result = []
        curr = self.head
        while curr.next:
            curr = curr.next
            result.append(curr.data)
        return result

    def concat(self, L):
        self.tail.next = L.head.next
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount

    def popAfter(self, prev):
        # (1) prev가 마지막 노드일때 (prev.next == None) -> return None
        # (2) 리스트 맨 끝의 노드를 삭제할 때 (curr.next == None) -> tail 조정 필요

        curr = prev.next
        if curr is None:
            return None

        prev.next = curr.next
        if curr.next is None:
            self.tail = prev

        self.nodeCount -= 1

        return curr.data

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

        prev = self.head
        ptr = self.head
        if pos == 1:
            return self.popAfter(prev)

        else:
            for _ in range(pos):
                prev = ptr
                ptr = ptr.next
            return self.popAfter(prev)
