from pydantic import BaseModel
class URLResponseModel(BaseModel):
    status: str
    message: str
    data: dict