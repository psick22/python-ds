from __future__ import annotations
from typing import Any, Type

null = -1


class Node:

    def __init__(self, data=null, next=null, dnext=null):
        self.data = data
        self.next = next
        self.dnext = dnext


class ArrayLinkedListIterator:

    def __init__(self, arr, head: int):
        self.arr = arr
        self.current = head

    def __iter__(self) -> ArrayLinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current == null:
            raise StopIteration
        else:
            data = self.arr[self.current].data
            self.current = self.arr[self.current].next
            return data


class ArrayLinkedList:

    def __init__(self, capacity: int):
        self.head = null
        self.current = null
        self.max = null
        self.deleted = null
        self.capacity = capacity
        self.arr = [Node()] * self.capacity
        self.no = 0

    def __len__(self) -> int:
        return self.no

    def get_insert_index(self):
        """다음 삽입할 레코드의 인덱스를 구함"""
        if self.deleted == null:  # 삭제 레코드가 없을 때 -> 하나도 삭제되지 않았거나 꽉차있거나
            if self.max + 1 < self.capacity:
                self.max += 1
                return self.max
            else:
                return null
        # 삭제 레코드가 있을 떄
        else:
            rec = self.deleted
            self.deleted = self.arr[rec].dnext
            return rec

    def delete_index(self, idx: int) -> None:
        """레코드 idx를 프리리스트에 등록"""
        if self.deleted == null:  # 삭제 레코드가 없을 때,
            self.deleted = idx
            self.arr[idx].dnext = null
        else:
            rec = self.deleted
            self.deleted = idx
            self.arr[idx].dnext = rec

    def search(self, data: Any) -> int:
        """ data와 값이 같은 노드를 검색 """
        idx = 0
        ptr = self.head
        while ptr != null:
            if self.arr[ptr].data == data:
                self.current = ptr
                return idx
            idx += 1
            ptr = self.arr[ptr].next

        return null

    def __contains__(self, data: Any) -> bool:
        return self.search() >= 0

    def add_first(self, data: Any) -> None:

        ptr = self.head
        rec = self.get_insert_index()
        if rec != null:
            self.head = self.current = rec
            self.arr[self.head] = Node(data, ptr)
            self.no += 1

    def add_last(self, data: Any) -> None:
        if self.head == null:
            self.add_first(data)

        else:
            ptr = self.head
            while self.arr[ptr].next != null:
                ptr = self.arr[ptr].next
            rec = self.get_insert_index()

            if rec != null:
                self.arr[ptr].next = self.current = rec
                self.arr[rec] = Node(data)
                self.no += 1

    def remove_first(self) -> None:
        if self.head != null:
            ptr = self.arr[self.head].next
            self.delete_index(self.head)
            self.head = self.current = ptr
            self.no -= 1

    def remove_last(self) -> None:
        if self.head != null:
            if self.arr[self.head].next == null:
                self.remove_first()
            else:
                ptr = self.head
                pre = self.head
                while self.arr[ptr].next != null:
                    pre = ptr
                    ptr = ptr.next

                self.arr[pre].next = null
                self.delete_index(ptr)
                self.current = pre
                self.no -= 1

    def remove(self, rec: int) -> None:
        if self.head != null:
            if rec == self.head:
                self.remove_first()
            else:
                ptr = self.head
                while self.arr[ptr].next != rec:
                    ptr = self.arr[ptr].next
                    if ptr == null:
                        return
                self.arr[ptr].next = null
                self.delete_index(rec)
                self.arr[ptr].next = self.arr[rec].next
                self.current = ptr
                self.no -= 1

    def remove_current_node(self) -> None:
        self.remove(self.current)

    def clear(self) -> None:
        while self.head != null:
            self.remove_first()
        self.current = null

    def next(self) -> bool:
        if self.current == null or self.arr[self.current].next == null:
            return False
        self.current = self.arr[self.current].next
        return True

    def print_current_node(self) -> None:
        if self.current == null:
            print('주목 노드가 없습니다')
        else:
            print(self.arr[self.current].data)

    def print(self) -> None:
        ptr = self.head
        while self.arr[ptr].next != null:
            print(self.arr[ptr].data)
            ptr = self.arr[ptr].next

    def dump(self) -> None:
        for i in self.arr:
            print(f'[{i}] : {i.data} {i.next} {i.dnext}')

    def __iter__(self) -> ArrayLinkedListIterator:
        return ArrayLinkedListIterator(self.arr, self.head)
