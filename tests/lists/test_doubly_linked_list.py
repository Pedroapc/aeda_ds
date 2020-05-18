import unittest

from aed_ds.lists.doubly_linked_list import DoublyLinkedList
from aed_ds.tad_iterator import TwoWayIterator
from aed_ds.exceptions import *

class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = DoublyLinkedList()

    def test_insert_first(self):
        self.list.insert_first("element 1")
        self.assertEqual(self.list.get(0), "element 1")
        self.list.insert_first("element 2")
        self.list.insert_first("element 3")
        self.list.insert_first("element 4")
        self.list.insert_first("element 5")
        self.assertEqual(self.list.get(0), "element 5")

    def test_insert_last(self):
        self.list.insert_last("element 1")
        self.assertEqual(self.list.get(0), "element 1")
        self.list.insert_last("element 2")
        self.list.insert_last("element 3")
        self.list.insert_last("element 4")
        self.list.insert_last("element 5")
        self.assertEqual(self.list.get(4), "element 5")

    def test_insert_first_and_last(self):
        self.list = DoublyLinkedList()
        self.list.insert_first("element 1")
        self.list.insert_last("element 2")
        self.assertEqual(self.list.get(0), "element 1")
        self.assertEqual(self.list.get(1), "element 2")
    
    def test_insert(self):
        self.list.insert("element 1", 0)
        
        with self.assertRaises(InvalidPositionException):
            self.list.insert("element X", 10)
       
        self.list.insert("element 2", 1)
        self.list.insert("element 4", 2)
        self.list.insert("element 5", 3)
        self.list.insert("element 3", 2)
        self.assertEqual(self.list.get(0), "element 1")
        self.assertEqual(self.list.get(1), "element 2")
        self.assertEqual(self.list.get(2), "element 3")
        self.assertEqual(self.list.get(3), "element 4")
        self.assertEqual(self.list.get(4), "element 5")

    def test_remove_first(self):
        with self.assertRaises(EmptyListException):
            self.list.remove_first()
        self.list.insert_first("element 1")
        self.assertEqual(self.list.remove_first(),None)
        self.list.make_empty()
        self.list.insert_first("element 1")
        self.list.insert_last("element 2")
        self.list.remove_first()
        self.assertEqual(self.list.get_first(), "element 2")
        

    def test_remove_last(self):
        with self.assertRaises(EmptyListException):
            self.list.remove_last()
        self.list.insert_last("element 1")
        self.assertEqual(self.list.remove_last(),None)
        self.list.make_empty()
        self.list.insert_first("element 1")
        self.list.insert_last("element 2")
        self.list.insert_last("element 3")
        self.list.remove_last()
        self.assertEqual(self.list.get_last(), "element 2")


    def test_remove(self):
        with self.assertRaises(InvalidPositionException):
            self.list.remove(1)
        self.list.insert_first("element 1")
        self.assertEqual(self.list.remove(0), None)
        self.list.insert_first("element 1")
        self.list.insert_last("element 2")
        self.list.insert_last("element 3")
        self.assertEqual(self.list.remove(1), "element 3")
        self.list.make_empty()
        self.list.insert_first("element 1")
        self.list.insert_last("element 2")
        self.list.insert_last("element 3")
        self.assertEqual(self.list.remove(2), None)
        
        

    def test_iterator(self):
        self.assertIsInstance(self.list.iterator(), TwoWayIterator)