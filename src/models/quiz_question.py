import sqlalchemy as sa

from src.core.database_config import Base


class QuizQuestion(Base):
    __tablename__ = "quiz_questions"

    id = sa.Column(sa.Integer, primary_key=True)
    question_id = sa.Column(sa.Integer, nullable=False)
    question = sa.Column(sa.String, nullable=False, unique=True)
    answer = sa.Column(sa.String, nullable=False)
    created_at = sa.Column(sa.DateTime)


