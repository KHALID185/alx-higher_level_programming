#!/usr/bin/python3
"""a class for singly linked list"""


class Node:
    """a singly linked list presentation"""

    def __init__(self, data, next_node=None):
        """Initialize a node with arguments"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """set a value"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for the next_node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Set a new_nd next_node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """a singly linked list"""

    def __init__(self):
        """Initalization"""
        self.__head = None

    def sorted_insert(self, value):
        """insert a new_nd value (argument)"""
        new_nd = Node(value)
        if self.__head is None:
            new_nd.next_node = None
            self.__head = new_nd
        elif self.__head.data > value:
            new_nd.next_node = self.__head
            self.__head = new_nd
        else:
            garage = self.__head
            while (garage.next_node is not None and
                    garage.next_node.data < value):
                garage = garage.next_node
            new_nd.next_node = garage.next_node
            garage.next_node = new_nd

    def __str__(self):
        """prints the inserting data"""
        data_insrt = []
        garage = self.__head
        while garage is not None:
            data_insrt.append(str(garage.data))
            garage = garage.next_node
        return ('\n'.join(data_insrt))
