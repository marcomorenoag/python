import React from 'react';
import TodoItem from "./Todo";

const TodoListView = (props) => {
  return (
    <div>
      <ul>
        {props.todoList.map((todo) => 
          <TodoItem todo={todo} />
        )}
      </ul>
    </div>
  )
}

export default TodoListView
