from fastapi import FastAPI,HTTPException
from enum import Enum
from typing import Optional
from pydantic import BaseModel



app = FastAPI(title="Demo API", description="A todo application", version="1.0.0")

class Task(BaseModel):
    
    title: str
    description: Optional[str] = None
    completed: bool = False
tasks={}
next_id=1
@app.get("/")
def home():
    return {"message": "Welcome to todo list app!"}

@app.post("/tasksadd/")
async def create_task(task: Task):
    global next_id
    new_task={
        "id": next_id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed
    }
    tasks[next_id] = new_task
    next_id += 1
    return new_task

@app.get("/tasks/")
async def get_tasks():
    return list(tasks.values())

@app.get("/tasks/{task_id}")
def get_task(task_id: int,updated_task: Task):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]

@app.put("/tasks/{task_id}")
def task_update(task_id:int, updated_task: Task):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id] = {
        "id": task_id,
        "title": updated_task.title,
        "description": updated_task.description,
        "completed": updated_task.completed
     }
    return tasks[task_id]


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return {"message": "Task deleted successfully"} 
