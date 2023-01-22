from TodoItem import todo_item

if __name__ == "__main__":

    todo1 = todo_item()
    todo2 = todo_item()
    todo1.add_todoItem("Buy bread")
    todo2.add_todoItem("Buy drinks")

    todo1.print_item()
    todo2.print_item()