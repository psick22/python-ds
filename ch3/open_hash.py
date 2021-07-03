from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib


# 버킷의 속성
class Status(Enum):
    OCCUPIED = 0
    EMPTY = 1
    DELETED = 2


class Bucket:
    def __init__(self, key: Any = None, value: Any = None, status: Status = Status.EMPTY) -> None:
        self.key = key
        self.value = value
        self.status = status

    def set(self, key: Any, value: Any, status: Status) -> None:
        self.key = key
        self.value = value
        self.status = status

    def set_status(self, status: Status) -> None:
        self.status = status


class OpenHash:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [Bucket()] * self.capacity

    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return (int(hashlib.md5(str(key).encode()).hexdigest(), 16) % self.capacity)

    def rehash_value(self, key: Any) -> int:
        return (self.hash_value(key) + 1) % self.capacity

    def search_node(self, key: Any) -> Any:
        """키가 key인 버킷을 검색"""
        hash = self.hash_value(key)
        node = self.table[hash]

        for i in range(self.capacity):
            if node.status == Status.EMPTY:
                break
            elif node.status == Status.OCCUPIED and node.key == key:
                return node
            hash = self.rehash_value(hash)
            node = self.table[hash]

        return None

    def search(self, key: Any) -> Any:
        node = self.search_node(key)
        if node is not None:
            return node.value
        else:
            return None

    def add(self, key: Any, value: Any) -> bool:
        if self.search(key) is not None:
            return False

        hash = self.hash_value(key)
        node = self.table[hash]
        for i in range(self.capacity):
            if node.status == Status.EMPTY or node.status == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True

            hash = self.rehash_value(key)
            node = self.table[hash]
        return False

    def remove(self, key: Any) -> int:
        node = self.search(key)
        if node is None:
            return False
        node.set_status(Status.DELETED)
        return True

    def dump(self) -> None:
        for i in range(self.capacity):
            print(f'{i:2} ', end='')
            if self.table[i].status == Status.OCCUPIED:
                print(f'{self.table[i].key} ({self.table[i].value})')
            elif self.table[i].status == Status.EMPTY:
                print('----미등록----')
            elif self.table[i].status == Status.DELETED:
                print('----삭제완료----')
