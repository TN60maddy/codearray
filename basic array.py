class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Array:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an Empty Array.")
        value = self.tail.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = None
            self.tail = current
        self.count -= 1
        return value

    def is_empty(self):
        return self.count == 0

    def get_elements(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(current.value)
            current = current.next
        return elements

    def search(self, value):
        current = self.head
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        raise ValueError("Item not found in the Array.")

    def index(self, value):
        current = self.head
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        raise ValueError("Item not found in the Array.")

    def sort(self, ascending=True):
        if ascending:
            self.is_sort()
        else:
            self.is_sort_descending()

    def is_sort(self):
        if self.count <= 1:
            return
        for i in range(self.count - 1):
            current = self.head
            for j in range(self.count - 1 - i):
                if current.value > current.next.value:
                    current.value, current.next.value = current.next.value, current.value
                current = current.next

    def is_sort_descending(self):
        if self.count <= 1:
            return
        for i in range(self.count - 1):
            current = self.head
            for j in range(self.count - 1 - i):
                if current.value < current.next.value:
                    current.value, current.next.value = current.next.value, current.value
                current = current.next
                
    def length(self):
        return self.count

my_array = Array()
my_array.push(40)
my_array.push(26)
my_array.push(80)
my_array.push(52)
print(my_array.get_elements())
pop_value = my_array.pop()
print(pop_value)
search_value = int(input("Enter an Search Value : "))
search = my_array.search(search_value)
print(f"The value is present in the Array at the index position of {search}.")
index_value = int(input("Enter an Value for an Index position : "))
index = my_array.index(index_value)
print(f"Index Position {index}.")
my_array.sort(ascending = False5)
sort_values = my_array.get_elements()
print(f"sorted Array {sort_values}.")
