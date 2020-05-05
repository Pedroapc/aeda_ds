from nodes import SingleListNode
from singlylinkedlistiterator import SinglyLinkedListIterator
import exceptions

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_element = 0
 # Returns true iff the list contains no elements.
    def is_empty(self):
        if self.head is None:
            return True
        return False

    # Returns the number of elements in the list.
    def size(self):
        return self.num_elements


    # Returns the first element of the list.
    # Throws EmptyListException.
    def get_first(self):
        if self.is_empty():
            raise EmptyListException()
        return self.head.get_element()

    # Returns the last element of the list.
    # Throws EmptyListException.
    def get_last(self):
        if self.is_empty():
            raise EmptyListException()
        return self.tail.get_element()

    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    def get(self, position):
        if self.is_empty():
            raise EmptyListException()
        count = 0
        current = self.head
        while count < self.num_elements:
            if count == position:
                return current.get_element()
            current = current.get_next()
            count += 1


    # Returns the position in the list of the
    # first occurrence of the specified element,
    # or -1 if the specified element does not
    # occur in the list.
    def find(self, element):
        count = 0
        current = self.head
        while count < self.num_elements:
            if current.get_element() == element:
                return count
            current = current.get_next()
            count += 1
        return -1

    # Inserts the specified element at the first position in the list.
    def insert_first(self, element):
        node = SingleListNode(element, self.head)
        self.head = node
        self.num_element += 1
        if self.tail is None:
            self.tail = self.head


    # Inserts the specified element at the last position in the list.
    def insert_last(self, element):
        if self.num_elements == 0:
            node = SingleListNode(element, None)
            self.tail = node
            self.head = self.tail
            self.num_elements += 1
        else:
            previous = self.tail
            node = SingleListNode(element, None)
            self.tail = node
            self.num_elements += 1
            previous.set_next(self.tail)  

    # Inserts the specified element at the specified position in the list.
    # Range of valid positions: 0, ..., size().
    # If the specified position is 0, insert corresponds to insertFirst.
    # If the specified position is size(), insert corresponds to insertLast.
    # Throws InvalidPositionException.
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
                    if index == position - 1:
                        node = SingleListNode(element, current.get_next())
                        current.set_next(node)
                        break
                    current = current.get_next()
                    index += 1
        

    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.
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
            self.num_elements -= 1
            return temp.get_element()
    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
    def remove_last(self):
        if self.num_elements == 1:
            self.head = None
            self.tail = None
            self.num_elements = 0
            return None
        elif self.num_elements == 0:
            raise EmptyListException()
        else:
            cur = self.head
            var = None
            while True:
                if cur.get_next() is None:
                    break
                var = cur
                cur = cur.get_next()
            
            self.tail = var
            self.tail.set_next(None)
            self.num_elements -= 1
            return self.tail.get_element()
    
    # Removes and returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException.
    def remove(self, position):
        if position == 0:
            self.remove_first()
        elif position == self.size()-1:
            self.remove_last()
        else:
            current = self.head
            index = 0
            while True:
                if index == position - 1:
                    temp = current.get_next()
                    current.set_next(temp.get_next())
                    return temp.get_element()

                current = current.get_next()
                index += 1
    
    # Removes all elements from the list.
    def make_empty(self):
        self.head = None
        self.tail = None
        self.num_elements = 0
    # Returns an iterator of the elements in the list (in proper sequence).
    def iterator(self):
        iterator = SinglyLinkedListIterator(self.head)
        result = ''
        verify = True
        while True:
            result += str(iterator.next()) + ' '

            if verify == False:
                break

            if not iterator.has_next():
                verify = False

        return result
