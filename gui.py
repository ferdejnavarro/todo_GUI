import functions
import FreeSimpleGUI as sg

label = sg.Text('Type a to-do')
input_box = sg.InputText(tooltip="Enter your to-do", key='todo')
button = sg.Button('Add')

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, button]],
                   font=('Helvetica', 16))

while True:
    event, value = window.read()
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = value['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()