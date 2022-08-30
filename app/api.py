from fastapi import FastAPI

from app.routers import data_router, graph_router, model_router

API = FastAPI(
    title="Prototype Iota - Finished",
    version="0.1.0",
    docs_url="/",
)


@API.post("/info", tags=["General Operations"])
async def info():
    return {"info": "API Information"}


for router in (data_router, graph_router, model_router):
    API.include_router(router.Router)
