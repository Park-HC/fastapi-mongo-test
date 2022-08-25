from typing import Optional, Union, List
from fastapi import UploadFile, File

from pydantic import BaseModel, Field

class ArticleSchema(BaseModel):
    title: str = Field(...)
    content: Union[str, None] = None
    files: List[UploadFile] = []

class UpdateArticleModel(BaseModel):
    title: Optional[str]
    content: Optional[str]
    files: Optional[List[UploadFile]] = None

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
