class Array:
    def __init__(self):
        self.values = []
        self.count = 0
    def push(self, value):
        self.values = self.values + [value]
        self.count += 1
    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an Empty Array.")
        value = self.values[-1]
        self.values = self.values[:-1]
        self.count -= 1
        return value
    def is_empty(self):
        return self.count == 0
    def get_elements(self):
        return self.values
    def search (self,value):
        for i in range(self.count):
            if self.values[i] == value:
                return i
        raise ValueError("Item not found in the Array.")
    def index (self,value):
        for i in range(self.count):
            if self.values[i] == value:
                return i
        raise ValueError("Item not found in the Array.")
    def sort(self):
        self.is_sort(0, self.size - 1)
    def is_sort(self, low, high):
        if low < high:
            pivot_index = self._partition(low, high)
            self.is_sort(low, pivot_index - 1)
            self.is_sort(pivot_index + 1, high)
    def _partition(self, low, high):
        pivot_value = self.values[high]
        i = low - 1
        for j in range(low, high):
            if self.values[j] <= pivot_value:
                i += 1
                self.values[i], self.values[j] = self.values[j], self.values[i]
        self.values[i + 1], self.values[high] = self.values[high], self.values[i + 1]
        return i + 1
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
my_array.sort()
sort_values = my_array.get_elements()
print(f"sorted Array {sort_values}.")
