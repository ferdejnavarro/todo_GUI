FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """
    Opens todos.txt file and returns the list of todos
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """
    Opens todos.txt and overwrites with the new list of todos
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

def get_help():
    return """Welcome to todo_app! Here we show you how you can take advantage of our newest app:\n
    COMMANDS\n
-Add: Type your todo item on the input box, then click "add" to add your new to-do to your list.
-Edit: Select a to-do item and type the new to-do on the input box. Then, click 'Edit' to modify your to-do.
-Complete: Select a to-do from the list and then click "complete" to eliminate the selected to-do from the list.            
-Clear: Type clear to eliminate your whole todo list.
-Exit: Select the "exit" button to exit the program."""

if __name__ == '__main__':
    print(get_todos())
    print(get_help())