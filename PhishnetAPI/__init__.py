from fastapi import FastAPI

app = FastAPI(title="Phishnet API",version="V0.0.1",description="API for Phishnet project")

from PhishnetAPI import router