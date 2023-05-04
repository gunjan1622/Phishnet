from pydantic import BaseModel

class URLRequestModel(BaseModel):
    is_phishing: bool
    confidence: float