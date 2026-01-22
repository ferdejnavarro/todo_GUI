import functions
import FreeSimpleGUI as sg

label = sg.Text('Type a to-do')
input_box = sg.InputText(tooltip="Enter your to-do", key='todo')
button = sg.Button('Add')
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45,10])
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete Todo', key='complete')
exit_button = sg.Button('Exit App', key='exit')
label_blank_space = sg.Text(' ', size=(24,1))


window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, button],
                           [list_box, edit_button],
                           [complete_button,label_blank_space,exit_button]],
                   font=('Helvetica', 16))

while True:
    event, values = window.read()
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'].strip('') + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'Edit':
            todo_to_edit = values['todos'][0]
            edited_todo = values['todo'].strip('') + '\n'

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = edited_todo
            functions.write_todos(todos)

            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'complete':
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'exit':
            break
        case sg.WIN_CLOSED:
            break

window.close()