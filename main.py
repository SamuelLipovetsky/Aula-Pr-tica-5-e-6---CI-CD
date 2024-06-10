
class TodoList:
    def __init__(self):
        self.todo_list = {}  

    def add_item(self, item):
        if item not in self.todo_list.keys():
            self.todo_list[item] = 0
            return str(item) + " added to list"
        else:
            return str(item) + " already in list"

    def remove_item(self, item):
        if item in self.todo_list.keys():
            self.todo_list.pop(item)
            return str(item) + " removed from list"
        else:
            return str(item) + " not in list"

    def mark_item_as_completed(self, item):
        if item in self.todo_list.keys():
            self.todo_list[item] = 1
            return str(item) + " done"
        else:
            return str(item) + " not in list"

    def mark_item_as_uncompleted(self, item):
        if item in self.todo_list.keys():
            self.todo_list[item] = 0
            return str(item) + " undone"
        else:
            return str(item) + " not in list"

    def show_completed_items(self):
        completed_items = [
            item for item in self.todo_list.keys() if self.todo_list[item] == 1
        ]
        return completed_items

    def show_uncompleted_items(self):
        uncompleted_items = [
            item for item in self.todo_list.keys() if self.todo_list[item] == 0
        ]
        return uncompleted_items

    def show_all_items(self):
        all_items = {
            item: ("completed" if status == 1 else "uncompleted")
            for item, status in self.todo_list.items()
        }
        return all_items


def handle_command(todo_list, command):
    command = command.strip().split()
    if not command:
        return "No command given"
    action = command[0].lower()
    if action == "add":
        item = " ".join(command[1:])
        return todo_list.add_item(item)
    elif action == "remove":
        item = " ".join(command[1:])
        return todo_list.remove_item(item)
    elif action == "complete":
        item = " ".join(command[1:])
        return todo_list.mark_item_as_completed(item)
    elif action == "uncomplete":
        item = " ".join(command[1:])
        return todo_list.mark_item_as_uncompleted(item)
    elif action == "show":
        sub_action = command[1].lower() if len(command) > 1 else ""
        if sub_action == "completed":
            completed_items = todo_list.show_completed_items()
            return f"Completed items: {completed_items}"
        elif sub_action == "uncompleted":
            uncompleted_items = todo_list.show_uncompleted_items()
            return f"Uncompleted items: {uncompleted_items}"
        elif sub_action == "all":
            all_items = todo_list.show_all_items()
            all_items_str = "\n".join(
                [f"{item}: {status}" for item, status in all_items.items()]
            )
            return f"All items:\n{all_items_str}"
        else:
            return "Unknown show command. Use 'show completed', 'show uncompleted', or 'show all'."
    elif action == "exit":
        return "exit"
    else:
        return "Unknown command. Available commands: add, remove, complete, uncomplete, show, exit."


def main():
    todo_list = TodoList()

    while True:
        command = input("Enter a command: ")
        result = handle_command(todo_list, command)
        if result == "exit":
            break
        print(result)


if __name__ == "__main__":
    main()
