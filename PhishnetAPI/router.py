from PhishnetAPI import app
# from .models.FrontendResponseSchema import URLResponse
# from .models import RequestBodySchema
from .core.ExceptionHandlers import *
from .core.Exceptions import *
from .services.Address import AddressBar

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

# @app.get("/api/response_check", response_model=URLResponseModel, tags=["Resource Server"])
# def api_response_check():
#     response_result = {
#         "status": "not_allowed",
#         "message": ["Not allowed to access this resource"],
#         "data": {},
#     }
#     # try:
#     #     db_msg = ""
#     #     if get_db_conn_flag():
#     #         db_msg = "Connection Successful to db!"
#     #     else:
#     #         db_msg = "Connection failed to db"

#     #     response_result["message"].append(db_msg)

#     # except Exception as e:
#     #     print("Exception :", e)

#     return response_result

# @app.post("/api/post_url", response_model=RequestBodySchema, tags=["Resource Server"])
# def post_url(responses: RequestBodySchema):
#     response_result={
#         "status": "not_allowed",
#         "message": ["No url provided"],
#         "data": {},
#     }
#     try:
#         url = responses.url
#         if url:
#             response_result["status"] = "allowed"
#             response_result["message"] = ["Url provided"]
#             response_result["data"] = {"url": url}
#         else:
#             response_result["message"] = ["No url provided"]
#     except Exception as e:
#         print("Exception :", e)

#     return response_result

# @app.get("/api/get_url", response_model=RequestBodyModel, tags=["Resource Server"])
# def get_url(responses: URLResponse):
#     response_result={
#         "status": "not_allowed",
#         "message": ["No url provided"],
#         "data": {},
#     }

