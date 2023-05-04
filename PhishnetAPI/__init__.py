from fastapi import FastAPI
# from PhishnetAPI.utils.DBConnection import DBConnection

app = FastAPI(title="Phishnet API",version="V0.0.1",description="API for Phishnet project")

from PhishnetAPI import router

# inits
# try:
#     dbconnection = DBConnection()
#     print(f"Connection successful:{dbconnection.get_client()}")
# except Exception as e:
#     print(e)