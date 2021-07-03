from __future__ import annotations
from typing import Sequence, Any
import hashlib


class Node:
    def __init__(self, key: Any, value: Any, next: Node) -> None:
        self.key = key
        self.value = value
        self.next = next


class ChainedHash:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [None] * self.capacity

    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity

    def search(self, key: Any) -> Any:
        """ 키가 key인 원소를 검색하여 값을 반환 """
        hash = self.hash_value(key)
        node = self.table[hash]

        while node is not None:
            if node.key == key:
                return node.value
            node = node.next

        return None

    def add(self, key: Any, value: Any) -> bool:
        """ 키가 key이고 값이 value인 원소 추가 """
        hash = self.hash_value(key)
        node = self.table[hash]

        while node is not None:
            if node.key == key:
                return False
            node = node.next

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True

    def remove(self, key: Any) -> bool:
        """ 키가 key인 원소를 삭제 """
        hash = self.hash_value(key)
        node = self.table[hash]
        prevNode = None

        while node is not None:
            if node.key == key:
                if prevNode is None:
                    self.table[hash] = node.next
                else:
                    prevNode.next = node.next

                prevNode = node
                node = node.next
            return False

    def dump(self) -> None:
        """ 해시테이블 전체 출력 """
        for i in range(self.capacity):
            node = self.table[i]
            print(i, end='')
            while node is not None:
                print(f' -> {node.key} ({node.value})', end='')
                node = node.next
            print()
