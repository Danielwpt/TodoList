class todo_item:
    
    def __init__(self):
        self.item_list = []

    def add_todoItem(self, item):
        self.item_list.append(item)

    def create_file(self, file_name):

        with open(file_name, "a") as file:
            for items in self.item_list:
                file.write(items + "\n")
        file.close()

    def print_item(self):
        print(self.item_list)