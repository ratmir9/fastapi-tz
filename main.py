import uvicorn

from src import app
from src.core.settings import settings

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=True
    )