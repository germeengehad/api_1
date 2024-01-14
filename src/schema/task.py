from pydantic import BaseModel
class Task(BaseModel):
    task_code: str
    task_type: str

class Score(BaseModel):
    task_score: int
    score_type: str