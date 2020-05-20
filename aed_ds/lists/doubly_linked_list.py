from .singly_linked_list import SinglyLinkedList
from .nodes import DoubleListNode
from .doubly_linked_list_iterator import DoublyLinkedListIterator
from ..exceptions import EmptyListException, NoSuchElementException, InvalidPositionException

class DoublyLinkedList(SinglyLinkedList):
    def __init__(self):
        SinglyLinkedList.__init__(self)

    def insert_first(self, element):
        self.head = DoubleListNode(element, self.head, None)
        if self.tail is None:
            self.tail = self.head
        self.num_elements += 1

    def insert_last(self, element):
        if self.num_elements == 0:
            self.head = DoubleListNode(element, None, None)
            self.tail = self.head
            self.num_elements += 1
        else:
            previous = self.tail
            node = DoubleListNode(element, None, previous)
            self.tail = node
            previous.set_next(self.tail) 
            self.num_elements += 1

    def insert(self, element, position):
        if position < 0 or position > self.size():
            raise InvalidPositionException()
        else: 
            if position == 0:
                self.insert_first(element)
            elif position == self.size():
                self.insert_last(element)
            else:
                current = self.head
                index = 0
                while True:
                    if index == position:
                        previous = current.get_previous()
                        node = DoubleListNode(element, current, previous)
                        previous.set_next(node)
                        current.set_previous(node)
                        break
                    current = current.get_next()
                    index += 1

                self.num_elements += 1

    def remove_first(self):
        if self.num_elements == 1:
            old_head = self.head
            self.head = None
            self.tail = None
            self.num_elements = 0
            return old_head.get_element()
        elif self.num_elements == 0:
            raise EmptyListException()
        else:
            old_head = self.head
            temp = self.head
            temp = self.head.get_next()
            self.head = temp
            self.head.set_previous(None)
            self.num_elements -= 1
            return old_head.get_element()

    def remove_last(self):
        if self.num_elements == 1:
            old_tail = self.tail
            self.head = None
            self.tail = None
            self.num_elements = 0
            return old_tail.get_element()
        elif self.num_elements == 0:
            raise EmptyListException()
        else:
            old_tail = self.tail
            var = self.tail.get_previous()
            self.tail = var
            self.tail.set_next(None)
            self.num_elements -= 1
            return old_tail.get_element()

    def remove(self, position):
        if position < 0 or position >= self.size():
            raise InvalidPositionException()
        else:
            if position == 0:
                return self.remove_first()
            elif position == (self.size()-1):
                return self.remove_last()
            else:
                current = self.head
                index = 0
                while True:
                    if index == position:
                        old_node = current
                        temp = current.get_next()
                        temp_previous = current.get_previous()
                        temp.set_previous(temp_previous)
                        temp_previous.set_next(temp)
                        self.num_elements -= 1
                        return old_node.get_element()

                    current = current.get_next()
                    index += 1

    def iterator(self):
        return DoublyLinkedListIterator(self)
                