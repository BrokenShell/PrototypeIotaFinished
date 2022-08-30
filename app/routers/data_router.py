from fastapi import APIRouter

Router = APIRouter(
    prefix="/data",
    tags=["Data Operations"],
)


@Router.post("/create")
async def create():
    return {"create": "insert new record"}


@Router.post("/read")
async def read():
    return {"read": "read record by id"}


@Router.post("/update")
async def update():
    return {"update": "updates an existing record"}


@Router.post("/delete")
async def delete():
    return {"delete": "delete record by id"}


@Router.post("/find")
async def find():
    return {"find": "find records by query"}


@Router.post("/reseed")
async def reseed():
    return {"reseed": "reseeds the database"}
