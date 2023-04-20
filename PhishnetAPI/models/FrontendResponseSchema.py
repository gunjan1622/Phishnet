from pydantic import BaseModel

class URLResponse(BaseModel):
    is_phishing: bool
    confidence: float