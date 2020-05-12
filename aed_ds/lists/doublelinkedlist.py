from aed_ds.lists.singlylinkedlist import SinglyLinkedList
from aed_ds.lists.nodes import DoubleListNode
from aed_ds.exceptions import EmptyListException, NoSuchElementException, InvalidPositionException

class DoubleLinkedList(SinglyLinkedList):
    def __init__(self):
        SinglyLinkedList.__init__(self)
        self.previous = None

    def get_previous(self):
        return self.previous

    def set_previous(self, previous):
        self.previous = previous
    
    def insert_first(self, element):
        node = DoubleListNode(element, self.head, None)
        self.head = node
        self.num_elements += 1
        if self.tail is None:
            node_tail = DoubleListNode(element, None, self.head)
            self.tail = node_tail

    def insert_last(self, element):
        if self.num_elements == 0:
            node = DoubleListNode(element, None, self.head)
            self.tail = node
            node_head = DoubleListNode(element, self.tail, None)
            self.head = node_head
            self.num_elements += 1
        else:
            previous = self.tail
            node = DoubleListNode(element, None, previous)
            self.tail = node
            self.num_elements += 1
            previous.set_next(self.tail) 

    def insert(self, element, position):
        if position > self.num_elements or position < self.num_elements:
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
            self.head = None
            self.tail = None
            self.num_elements = 0
            return None
        elif self.num_elements == 0:
            return EmptyListException()
        else:
            temp = self.head
            temp = self.head.get_next()
            self.head = temp
            self.head.set_previous(None)
            self.num_elements -= 1
            return temp.get_element()

    def remove_last(self):
        if self.num_elements == 1:
            self.head = None
            self.tail = None
            self.num_elements = 0
            return None
        elif self.num_elements == 0:
            raise EmptyListException()
        else:
            var = self.tail.get_previous()
            self.tail = var
            self.tail.set_next(None)
            self.num_elements -= 1
            return self.tail.get_element()

    def remove(self, position):
        if position < 0 and position >= self.size():
            raise InvalidPositionException()
        else:
            if position == 0:
                self.remove_first()
            elif position == self.size()-1:
                self.remove_last()
            else:
                current = self.head
                index = 0
                while True:
                    if index == position:
                        #tenho que ver
                        temp = current.get_next()
                        temp_previous = current.get_previous()
                        temp.set_previous(temp_previous)
                        temp_previous.set_next(temp)
                        self.num_elements -= 1
                        return temp.get_element()

                    current = current.get_next()
                    index += 1

                