import uvicorn
from fastapi import FastAPI
from api import router as api_router
from core.config import settings
from contextlib import asynccontextmanager
from core.models import db_helper

from fastapi.responses import ORJSONResponse  # ускорение сериализации и десериализации данных при парсинге json.


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()

app = FastAPI(lifespan=lifespan, default_response_class=ORJSONResponse)
app.include_router(api_router, prefix=settings.api.prefix)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host=settings.run.host, port=settings.run.port)

