from typing import Union

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.quiz_question import QuizQuestion


class QuizQuestionRepo:

    async def get_previous_quiz_question(self, session: AsyncSession) -> Union[QuizQuestion, None]:
        query = select(QuizQuestion).order_by(QuizQuestion.id.desc()).offset(1).limit(1)
        questions = await session.execute(query)
        return questions.scalar_one_or_none()

    async def get_quiz_questions_by_answer(self, session: AsyncSession, answer: str) -> Union[QuizQuestion, None]:
        query = select(QuizQuestion.id).filter_by(answer=answer)
        result = await session.execute(query)
        return result.first()

    async def create_quiz_question(self, session: AsyncSession, data_quiz_question: dict) -> QuizQuestion:
        query = insert(QuizQuestion).values(**data_quiz_question)
        await session.execute(query)
        await session.commit()


quiz_questions_repo = QuizQuestionRepo()
