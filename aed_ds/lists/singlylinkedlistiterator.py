from aed_ds import tad_iterator
from aed_ds.exceptions import EmptyListException, NoSuchElementException

class SinglyLinkedListIterator:
    def __init__(self, head):
        self.head = head
        self.current = head


# Returns true iff the iteration has more elements.
    # In other words, returns true next would return an element rather than throwing an exception.
    
    def has_next(self):
        return self.current.has_next()
    # Returns the next element in the iteration.
    # Throws NoSuchElementException
    
    def next(self):
        if not self.current:
            raise NoSuchElementException()
        cur = self.current
        self.current = self.current.get_next()
        return cur.get_element()


    # Restarts the iteration. After rewind, if the iteration is not empty, next will return the first element in the iteration.
    
    def rewind(self):
        if self.current != None:
            self.current = self.head
        else:
            raise EmptyListException()

