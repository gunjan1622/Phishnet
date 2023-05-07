from PhishnetAPI import app
from .models.FrontendResponseSchema import URLResponseModel
from .models.RequestBodySchema import URLRequestModel
from .core.ExceptionHandlers import *
from .core.Exceptions import *
from .services.Address import AddressBar
from .services import load_model

from fastapi import Request, Depends
from fastapi.middleware.cors import CORSMiddleware

from fastapi.templating import Jinja2Templates
from fastapi import Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# # template and static files setup
# templates = Jinja2Templates(directory="API/templates/")
# app.mount("/static", StaticFiles(directory="API/static"), name="static")

#Middleware to handle CORS (cross origin  resource sharing) error in the browser
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/",tags=["Home"])
def home(request: Request):
    return {"message": "Welcome to Phishnet API"}

@app.get("/api/response_check", response_model=URLResponseModel, tags=["Resource Server"])
def api_response_check():
    response_result = {
        "status": "not_allowed",
        "message": "No url provided",
        "data": {},
    }
    #check if the url is provided
    try:
        response_result["status"] = "allowed"
        response_result["message"] = "Url provided"
        response_result["data"] = {"url": AddressBar().get_url()}
    except Exception as e:
        print("Exception :", e)

    return response_result

@app.post("/api/post_url", response_model=URLResponseModel, tags=["Resource Server"])
def post_url(responses: URLResponseModel):
    response_result={
        "status": "not_allowed",
        "message": "No url provided",
        "data": {},
    }
    post_url=AddressBar.get_url()
    response_result["status"]="allowed"
    response_result["message"]="Url provided"
    response_result["data"]={"url":post_url}
    return response_result


@app.get("/api/get_url", response_model=URLRequestModel, tags=["Resource Server"])
def get_url(responses: URLRequestModel):
    response_result={
        "status": "not_allowed",
        "message": "No url provided",
        "data": {},
    }

    get_url["data"]["url"]=post_url()
    try:
        response_result["status"]="allowed"
        response_result["message"]="Url fecthed"
        response_result["data"]={"url":get_url}
    except Exception as e:
        print("Exception :", e)

    return response_result