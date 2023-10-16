from fastapi import APIRouter, Depends

from src.schemas.quiz_question import QuizQuestionsSchema
from src.services.quiz_question import QuizQuestionsService

router = APIRouter()


@router.post("/", response_model=QuizQuestionsSchema)
async def add_quiz_questions(
        questions_num: int,
        service: QuizQuestionsService = Depends()
):
    return await service.add_quiz_questions(questions_num)
