from fastapi import FastAPI

from server.routes.article import router as ArticleRouter

app = FastAPI()

app.include_router(ArticleRouter, tags=["Article"], prefix="/article")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
