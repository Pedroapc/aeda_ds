from .tad_dictionary import Dictionary
from ..exceptions import NoSuchElementException, DuplicatedKeyException
from ..lists.singly_linked_list import SinglyLinkedList
from .item import Item
import ctypes

class HashTable(Dictionary):
    def __init__(self, size = 101):
        self.vector = (size * ctypes.py_object)()
        self.list_keys = SinglyLinkedList()
        self.list_values = SinglyLinkedList()
        self.num_elements = 0
        self.arraySize = size

        for i in range(size):
            self.vector[i] = SinglyLinkedList()

    def size(self):
        return self.num_elements

    def is_full(self): 
        return self.num_elements == self.arraySize

    def get(self, k):
        value_hash = self.hash_function(k)

        it = self.vector[value_hash].iterator()
        while it.has_next():
            i = it.next()
            if i.get_key() == k:
                return i.get_value()

        raise NoSuchElementException


    def insert(self, k, v):
        value_hash = self.hash_function(k)
        item = Item(k,v)

        if self.has_key(k):
            raise DuplicatedKeyException()

        self.list_keys.insert_last(k)
        self.list_values.insert_last(v)
        self.vector[value_hash].insert_last(item)
        self.num_elements += 1


    def update(self, k, v):
        exist = False
        value_hash = self.hash_function(k)

        it = self.vector[value_hash].iterator()
        while it.has_next():
            i = it.next()
            if i.get_key() == k:
                i.set_value(v)
                exist = True
                break

        if not exist:
            raise NoSuchElementException


    def remove(self, k):
        value_hash = self.hash_function(k)

        index = 0
        it = self.vector[value_hash].iterator()
        while it.has_next():
            i = it.next()
            if i.get_key() == k:
                self.vector[value_hash].remove(index)
                self.num_elements -= 1
                return str(i.get_value())
            index += 1
        
        raise NoSuchElementException


    def keys(self):
        return self.list_keys

    def values(self):
        return self.list_values

    def items(self):
        list_items = SinglyLinkedList()

        for i in range(self.arraySize):
            it = self.vector[i].iterator()
            while it.has_next():
                cur = it.next()
                list_items.insert_last(cur)

        return list_items

    def hash_function(self, key):
        return sum([ord(c) for c in key]) % self.arraySize

    def has_key(self, key):
        value_hash = self.hash_function(key)
        it = self.vector[value_hash].iterator()
        while it.has_next():
            i = it.next()
            if i.get_key() == key:
                return True
            
        return False