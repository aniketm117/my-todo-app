import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("Add items to do and remember stuff.")

cnt = 0

for index, todo in enumerate(todos):
    cnt += 1
    checkbox = st.checkbox(todo[:-1], key=f"{todo[:-1]}_{cnt}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"{todo[:-1]}_{cnt}"]
        st.experimental_rerun()

st.text_input(label="Todo Item", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
