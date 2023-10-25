#!/usr/bin/python3
"""class that defines a node of a singly linked list"""


class Node:
    """class node of a linked list"""

    def __init__(self, data, next_node=None):
        """initialize the arguments"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter for the data in the ll"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter of data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter of the pointer to the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter of next node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """singly linked list class"""

    def __init__(self):
        """initialize arguments"""
        self.__head = None

    def sorted_insert(self, value):
        """ inserts a new Node into the correct sorted position"""
        n_d = Node(value)
        if self.__head is None:
            n_d.next_node = None
            self.__head = n_d
        elif self.__head.data > value:
            n_d.next_node = self.__head
            self.__head = n_d
        else:
            garage = self.__head
            while (garage.next_node is not None and
                    garage.next_node.data < value):
                garage = garage.next_node
                n_d.next_node = garage.next_node
                garage.next_node = n_d

    def __str__(self):
        """representation of the output"""

        DATA = []
        garage = self.__head
        while garage is not None:
            DATA.append(str(garage.data))
            garage = garage.next_node
        return("\n".join(DATA))
