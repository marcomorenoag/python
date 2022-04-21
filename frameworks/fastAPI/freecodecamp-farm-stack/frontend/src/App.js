import React, { useState, useEffect } from "react";
import axios from "axios";
import TodoListView from "./components/TodoListView";
import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";

function App() {
  const [todoList, setTodoList] = useState([{}]);
  const [title, setTitle] = useState("");
  const [desc, setDesc] = useState("");

  const addTodoHandler = () => {
    axios
      .post("http://localhost:8000/api/todo", {
        "title": title,
        "description": desc,
      })
      .then((res) => console.log(res));
  }

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/todo")
      .then((res) => {
        setTodoList(res.data)
      });
  }, []);

  return (
    <div
      className="App list-group-item justify-content-center align-items-center mx-auto"
      style={{ width: "400px", backgroundColor: "white", marginTop: "15px" }}
    >
      <h1 className="card text-white bg-primary mb-1" styleName="max-width: 20rem;">
        Task Manager
      </h1>
      <h6 className="card text-white bg-primary mb-3">FASTAPI - React - MongoDB</h6>
      <div className="card-body">
        <h5 className="card text-white bg-dark mb-3">Add Your Task</h5>
        <span className="card-text">
          <input className="mb-2 form-control titleIn" placeholder="Title" onChange={e => setTitle(e.target.value)}/>
          <input className="mb-2 form-control desIn" placeholder="Description" onChange={e => setDesc(e.target.value)}/>
          <button
            className="btn btn-outline-primary mx-2 mb-3"
            style={{ borderRadius: "50px", fontWeight: "bold " }}
            onClick={addTodoHandler}
          >
            Add Task
          </button>
        </span>

        <h5 className="card text-white bg-dark mb-3">Your Tasks</h5>
        <div>
          <TodoListView todoList={todoList} />
        </div>
        <h6 className="card text-dark bg-warning py-1 mb-0">Copyright 2021, all rights reserved</h6>
      </div>
    </div>
  );
}

export default App;
