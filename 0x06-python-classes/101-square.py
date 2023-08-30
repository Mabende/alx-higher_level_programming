#!/usr/bin/python3
"""
Module: singly_linked_list
"""

class Node:
    """
    Represents a node of a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node): The next node in the linked list.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new Node instance with data and optional next_node.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node): The next node in the linked list (default is None).

        Raises:
            TypeError: If data is not an integer or next_node is not None or a Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method to retrieve the data attribute.
        
        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method to set the data attribute.
        
        Args:
            value (int): The new data for the node.
            
        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method to retrieve the next_node attribute.
        
        Returns:
            Node: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method to set the next_node attribute.
        
        Args:
            value (Node): The new next_node for the node.
            
        Raises:
            TypeError: If next_node is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.

    Attributes:
        head: The head node of the linked list.
    """
    def __init__(self):
        """
        Initializes a new SinglyLinkedList instance with an empty head.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).
        
        Args:
            value (int): The value to be inserted into the linked list.
        """
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            return
        
        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return
        
        current = self.head
        while current.next_node and value >= current.next_node.data:
            current = current.next_node
        
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.
        
        Returns:
            str: A string representation of the linked list.
        """
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()

