from datetime import datetime

import requests
from fastapi import HTTPException
from starlette import status

from src.core.database_config import async_session_maker
from src.models.quiz_question import QuizQuestion
from src.repo.quiz_questions import quiz_questions_repo


class QuizQuestionsService:

    def modify_data(self, item: dict) -> dict:
        format_str = '%Y-%m-%dT%H:%M:%S.%fZ'
        quiz_question = {
            "question_id": item["id"],
            "question": item["question"],
            "answer": item["answer"],
            "created_at": datetime.strptime(item["created_at"], format_str)
        }
        return quiz_question

    def get_data_quiz_questions(self, params=None) -> list[dict]:
        url = "https://jservice.io/api/random"
        if params:
            response = requests.get(url, params)
        else:
            response = requests.get(url)
        if response.status_code:
            quiz_questions = response.json()
            if quiz_questions:
                return quiz_questions

    async def add_quiz_questions(self, questions_num: int) -> QuizQuestion:
        try:
            async with async_session_maker() as session:
                params = {"count": questions_num}
                data_quiz_questions = self.get_data_quiz_questions(params)
                for item in data_quiz_questions:
                    quiz_question = self.modify_data(item)
                    if not await quiz_questions_repo.get_quiz_questions_by_answer(session,
                                                                                  quiz_question['answer']):
                        await quiz_questions_repo.create_quiz_question(session, quiz_question)
                    else:
                        data_quiz_question = self.get_data_quiz_questions()
                        data_quiz_questions.append(data_quiz_question[0])
                return await quiz_questions_repo.get_previous_quiz_question(session)
        except Exception as err:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(err)
            )
