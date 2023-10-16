from datetime import datetime

from pydantic import BaseModel, ConfigDict


class QuizQuestionsSchema(BaseModel):
    id: int
    question_id: int
    question: str
    answer: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
