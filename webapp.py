import streamlit as lt
import Funct


def add_todo():
    todo = lt.session_state["new_todo"] + '\n'
    todos.append(todo)
    Funct.write_todos(todos)


todos = Funct.get_todos()

lt.title('My Todo App')
lt.subheader("A list of todo items")
lt.write('This is to learn webapps')

for index, todo in enumerate(todos):
    checking = lt.checkbox(todo, key=todo)
    if checking:
        todos.pop(index)
        Funct.write_todos(todos)
        del lt.session_state[todo]
        lt.experimental_rerun()

lt.text_input(label=' ', placeholder='Add a todo...', on_change=add_todo,
              key='new_todo')

