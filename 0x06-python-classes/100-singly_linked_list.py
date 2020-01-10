class Node:
    def __init__(self, data, next_node=None):
        self.next_node = next_node
        self.data = data
    
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            pass
        else:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None: 
            new_node.next_node = self.__head 
            self.__head = new_node 
  
        # Special case for __head at end 
        elif self.__head.data >= new_node.data: 
            new_node.next_node = self.__head 
            self.__head = new_node 
  
        else : 
  
            # Locate the node before the point of insertion 
            current = self.__head 
            while(current.next_node is not None and
                 current.next_node.data < new_node.data): 
                current = current.next_node
              
            new_node.next_node = current.next_node
            current.next_node = new_node 
  
    def __str__(self):
        temp = self.__head

        if not temp:
            return ''
        while not (temp.next_node is None): 
            print(temp.data) 
            temp = temp.next_node
        return str(temp.data)

