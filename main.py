from TodoItem import todo_item

if __name__ == "__main__":

    new_file_name = input("Enter new file name: ")

    item_list = input("Enter thing to do: ")

    todo1 = todo_item()

    todo1.add_todoItem(item_list)

    todo1.create_file(new_file_name + ".txt")