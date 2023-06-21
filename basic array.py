class Array:
    def __init__(self, capacity):
        self.values = []
        self.capacity = capacity
    def push(self, value):
        if len(self.values) < (self.capacity):
            self.values.append(value)
        else:
            raise IndexError("Array is Full.")
    def pop(self):
        if not self.is_empty():
            return self.values.pop()
        else:
            raise IndexError("Cannot pop from an Empty Array.")
    def is_empty(self):
        return len(self.values) == 0
    def get_elements(self):
        return self.values
    def search (self,value):
        if value in self.values:
            return self.values.index(value)
        else:
            raise ValueError ("Item Not found in the Array.")
    def index (self, value):
        if value in self.values:
            return self.values.index(value)
        else:
            raise ValueError ("Item Not found in the Array.")
    def is_sort(self):
        self.values.sort()

capacity = int(input("Enter the size of an Array : "))
my_array = Array(capacity)
for i in range (capacity):
    value = int(input("Enter the Element for Array {} : ".format(i)))
    my_array.push(value)
print(my_array.get_elements())
pop_value = my_array.pop()
print(pop_value)
search_value = int(input("Enter an Search Value : "))
search = my_array.search(search_value)
print(f"The value is present in the Array at the index position of {search}.")
index_value = int(input("Enter an Value for an Index position : "))
index = my_array.index(index_value)
print(f"Index Position {index}.")
my_array.is_sort()
sort_values = my_array.get_elements()
print(f"sorted Array {sort_values}.")
