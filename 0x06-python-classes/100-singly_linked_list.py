#!/usr/bin/python3
"""singly linked list module"""


class Node:
    """"defines a node"""

    def __init__(self, data, next_node=None):
        """initializes the node with instance variables"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """gets data attribute"""

        return (self.__data)

    @data.setter
    def data(self, value):
        """sets data attribute"""

        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def nxt_node(self):
        """get nxt_node attribute
        Returns: next node
        """

        return (self.__nxt_node)

    @nxt_node.setter
    def nxt_node(self, value):
        """set value of next node"""

        if (value is not None and not isinstance(value, Node)):
            raise TypeError('nxt_node must be a Node object')

        self.__nxt_node = value


class SinglyLinkedList:
    """defines a singly linked list"""

    def __init__(self):
        """Initializes the singly linked list"""

        self.head = None

    def __str__(self):
        """make list printable"""

        printsll = ""
        locn = self.head
        while locn:
            printsll += str(locn.data) + "\n"
            locn = locn.nxt_node
        return printsll[:-1]

    def sorted_insert(self, value):
        """insert in a sorted fashion
        Args:
            value: what the value will be on the node
        """
        new = Node(value)
        if not self.head:
            self.head = new
            return
        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return
        locn = self.head
        while locn.nxt_node and locn.nxt_node.data < value:
            locn = locn.nxt_node
        if locn.nxt_node:
            new.nxt_node = locn.nxt_node
        locn.nxt_node = new
