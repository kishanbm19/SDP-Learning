from pydantic import BaseModel, Field,config


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)


class TaskResponse(BaseModel):
    id: int
    title: str
    completed:bool

    model_config = {"from_attributes": True}

class TaskUpdate(BaseModel):
    completed:bool

