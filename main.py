from functions import get_todos, write_todos, get_help
import time

todos = []
print('Welcome to todo_app!')

now = time.strftime('%b %d, %Y, %H:%M:%S')
print('It is', now)
while True:
    # Get user input, strip space characters if necessary
    prompt = input('Please type add, edit, complete, show, clear, help or exit: ')
    prompt = prompt.strip()

    if prompt == 'add':
        print('Dont forget to add your todo next to the "add" command, for example: add walk with dog')

    elif prompt.startswith('add'):
        todo = prompt[4:]+'\n'
        todo = todo.capitalize()

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)

    elif prompt.startswith('show'):
        todos = get_todos()
        for index,item in enumerate(todos):
            item = item.strip('\n')
            iteration = f'{index + 1}.- {item}'
            print(iteration)

    elif prompt.startswith('complete'):
        try:
            todos = get_todos()

            todo_number = int(prompt[9:])

            print(f'{todo_number}.-{todos[todo_number - 1].strip('\n')} completed successfully, great job!')
            todos.pop(todo_number - 1)

            write_todos(todos)

        except IndexError:
            print('Invalid command, if you need help type "help"')
            continue

        except ValueError:
            print('Invalid command, if you need help type "help"')
            continue

    elif prompt.startswith('edit'):
        todos = get_todos()
        try:
            todo_number = int(prompt[5:])
            print(f'{todo_number}.- {todos[todo_number - 1].strip('\n')}')

            edited_todo = input('Type the new todo: ')
            todos[todo_number - 1] = edited_todo + '\n'
            print(f'Todo {todo_number} was successfully edited to {edited_todo}!')

            write_todos(todos)

        except ValueError:
            print('Invalid command, if you need help please type "help"')
            continue


    elif prompt.startswith('clear'):
        answer = input('Are you sure you want to clear your todo list? All todos will be erased, type yes or no: ')
        match answer:
            case 'yes':

                todos = []

                write_todos(todos)

            case 'no':
                break

    elif prompt.startswith('exit'):
        break

    elif prompt.startswith('help'):
        print(get_help())
        continue

    else:
        print('Invalid input, please enter an action alongside your "todo", for example "add Jog": ')

print('See you later')



