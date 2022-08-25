from typing import List

from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    retrieve_articles,
    retrieve_article,
    add_article,
    update_article,
    delete_article,
)
from server.models.article import (
    ArticleSchema,
    UpdateArticleModel,
    ResponseModel,
    ErrorResponseModel,
)

router = APIRouter()

@router.post("/", response_description="Article data added into the database")
async def add_article_data(article: ArticleSchema = Body(...)):
    article = jsonable_encoder(article)
    new_article = await add_article(article)
    return ResponseModel(new_article, "Article is successfully added")

@router.get("/", response_description="Articles retrived")
async def get_articles():
    articles = await retrieve_articles()
    if articles:
        return ResponseModel(articles, "Good!")
    return ResponseModel(articles, "None")

@router.get("/{id}", response_description="Article retrived")
async def get_article_data(id):
    article = await retrieve_article(id)
    if article:
        return ResponseModel(article, "Find it")
    return ErrorResponseModel("error!", 404, "not the one we have")

@router.put("/{id}")
async def update_student_data(id: str, req: UpdateArticleModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_success = await update_article(id, req)
    if updated_success:
        return ResponseModel(req, "update completed")
    return ErrorResponseModel(
        "upload Error!",
        404,
        "no! no!"
    )

@router.delete("/{id}")
async def delete_article_data(id: str):
    delete_success = await delete_article(id)
    if delete_success:
        return ("successfully removed")
    return("i cannot delete it")

from fastapi import UploadFile, File

@router.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile]):
    return {"filenames": [file.filename for file in files]}
