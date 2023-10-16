from fastapi import APIRouter

from src.api.quiz_question import router as quiz_question_router

router = APIRouter()
router.include_router(quiz_question_router,
                      prefix="/api/v1/question",
                      tags=["quiz questions"])
