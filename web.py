import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("Cold-Run")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo[:-1], key=todo[:-1])
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo[:-1]]
        st.experimental_rerun()

st.text_input(label="Todo Item", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')