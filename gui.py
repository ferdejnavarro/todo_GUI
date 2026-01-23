import functions
import FreeSimpleGUI as sg
import time

sg.theme('DarkGrey8')

clock = sg.Text('', key='clock')
label = sg.Text('Type a to-do')
input_box = sg.InputText(tooltip="Enter your to-do", key='todo', size=(46))
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(45, 10))
add_button = sg.Button('Add', bind_return_key=True)
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete Todo', key='complete')
exit_button = sg.Button('Exit App', key='exit')
help_button = sg.Button('Help', key='help')
clear_button = sg.Button('Clear', key='clear')

label_blank_space1 = sg.Text(' ', size=(15,1))
label_blank_space2 = sg.Text(' ', size=(24,1))
label_blank_space3 = sg.Text(' ', size=(37,1))


window = sg.Window('My To-Do App',
                   layout=[[label, help_button, label_blank_space1, clock],
                           [input_box, add_button],
                           [list_box, edit_button],
                           [complete_button,label_blank_space2],
                           [clear_button, label_blank_space3, exit_button]],
                   font=('Helvetica', 16))

while True:
    event, values = window.read(timeout=10)

    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'].strip('') + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                edited_todo = values['todo'].strip('') + '\n'

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = edited_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup('Please select a to-do item first', font=('Helvetica', 16))
                pass
        case 'todos':
            try:
                window['todo'].update(value=values['todos'][0])
            except IndexError:
                pass
        case 'complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)

                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                pass
        case 'clear':
            todos = []
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'help':
            sg.popup(functions.get_help())
        case sg.WIN_CLOSED | 'exit' | None:
            break
    window['clock'].update(str(time.strftime('%b %d, %Y, %H:%M:%S')))

window.close()