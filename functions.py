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
    -add: Type "add" followed by the todo you want to add to your list, for example: add walk with dog   
    -show: Type "show" to see your current todo list
    -complete: Type "complete" followed by its todo number to eliminate a todo from the list, if you need to see your todo list, please type "complete".            
    -edit: Type "edit" followed by the todo number to edit. If you need to see your todo list, please type "show", then "edit" and then you will be asked to type your new todo
    -clear: Type clear to eliminate your whole todo list.
    -exit: Type "exit" to exit the program."""

if __name__ == '__main__':
    print(get_todos())
    print(get_help())