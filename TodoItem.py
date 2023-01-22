class todo_item:
    
    def __init__(self):
        self.item_list = []

    def add_todoItem(self, item):
        self.item_list.append(item)

    def print_item(self):
        print(self.item_list)