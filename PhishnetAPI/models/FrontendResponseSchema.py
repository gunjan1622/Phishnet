from pydantic import BaseModel

class URLResponseModel(BaseModel):
    url: str