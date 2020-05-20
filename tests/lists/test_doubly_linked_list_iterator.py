import unittest

from aed_ds.lists.doubly_linked_list import DoublyLinkedList
from aed_ds.exceptions import NoSuchElementException

class TestDoublyLinkedListIterator(unittest.TestCase):
    def setUp(self): pass

    def test_has_next(self):
        doubly_linked_list = DoublyLinkedList()
        it = doubly_linked_list.iterator()
        self.assertFalse(it.has_next())
        doubly_linked_list.insert_last("element 1")
        doubly_linked_list.insert_last("element 2")
        doubly_linked_list.insert_last("element 3")
        it = doubly_linked_list.iterator()
        self.assertTrue(it.has_next())
        it.next()
        self.assertTrue(it.has_next())
        it.next()
        self.assertTrue(it.has_next())
        it.next()
        self.assertFalse(it.has_next())
        
    def test_next(self): 
        doubly_linked_list = DoublyLinkedList()
        it = doubly_linked_list.iterator()
        with self.assertRaises(NoSuchElementException):
            it.next()
        doubly_linked_list.insert_last("element 1")
        doubly_linked_list.insert_last("element 2")
        doubly_linked_list.insert_last("element 3")
        it = doubly_linked_list.iterator()
        self.assertEqual(it.next(), "element 1")
        self.assertEqual(it.next(), "element 2")
        self.assertEqual(it.next(), "element 3")
        with self.assertRaises(NoSuchElementException):
            it.next()         

    def test_rewind(self):
        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.insert_last("element 1")
        doubly_linked_list.insert_last("element 2")
        doubly_linked_list.insert_last("element 3")
        it = doubly_linked_list.iterator()
        self.assertEqual(it.next(), "element 1")
        self.assertEqual(it.next(), "element 2")
        it.rewind()
        self.assertEqual(it.next(), "element 1")

    def test_has_previous(self):
        doubly_linked_list = DoublyLinkedList()
        it = doubly_linked_list.iterator()
        self.assertFalse(it.has_previous())
        doubly_linked_list.insert_last("element 1")
        doubly_linked_list.insert_last("element 2")
        doubly_linked_list.insert_last("element 3")
        it = doubly_linked_list.iterator()
        it.full_forward()
        self.assertTrue(it.has_previous())
        it.previous()
        self.assertTrue(it.has_previous())
        it.previous()
        self.assertTrue(it.has_previous())
        it.previous()
        self.assertFalse(it.has_previous())

    
    def test_previous(self):
        doubly_linked_list = DoublyLinkedList()
        it = doubly_linked_list.iterator()
        with self.assertRaises(NoSuchElementException):
            it.previous()
        doubly_linked_list.insert_last("element 1")
        doubly_linked_list.insert_last("element 2")
        doubly_linked_list.insert_last("element 3")
        it = doubly_linked_list.iterator()
        it.full_forward()
        self.assertEqual(it.previous(), "element 3")
        self.assertEqual(it.previous(), "element 2")
        self.assertEqual(it.previous(), "element 1")
        with self.assertRaises(NoSuchElementException):
            it.previous()   



    def test_full_forward(self):
        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.insert_last("element 1")
        doubly_linked_list.insert_last("element 2")
        doubly_linked_list.insert_last("element 3")
        it = doubly_linked_list.iterator()
        it.full_forward()
        self.assertEqual(it.previous(), "element 3")