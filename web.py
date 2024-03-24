import streamlit as st
import functions

def add_todo():
    for item in todos:
        if st.session_state["new_todo"] + "\n" == item:
            st.warning("You have already entered this to-do item.")

    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("A Todo App")
with st.expander("About this app"):
    st.info("Add items to-do or simply note them down for future")

todos = functions.get_todos()

count = 0

for index, todo in enumerate(todos):
    count += 1
    checkbox = st.checkbox(todo[:-1], key=f"{todo[:-1]}-{count}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"{todo[:-1]}-{count}"]
        st.experimental_rerun()

st.text_input(label="Todo Item", placeholder="Add new todo",
              on_change=add_todo, key='new_todo')

"stats-for-nerds"

for the_todo in st.session_state.items():
    the_todo