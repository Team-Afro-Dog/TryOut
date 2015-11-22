class Node:
    def __init__(self, data, next_ptr):
        self.data = data
        self.next = next_ptr
    def get_data(self):
        return self.data
    def change_data(self, data):
        self.data = data
    def increment(self):
        self = self.next
    def change_next(self, next_ptr):
        self.next = next_ptr
    def print_node(self):
        print(self.data)
    def print_all_node(self):
        print(self.data)
        if(self.next != None):
            self.next.print_all_node()
    def __str__(self):
        return str(self.data)
