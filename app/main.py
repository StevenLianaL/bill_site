from fastapi import FastAPI

from app.db import database
from app.routers import bill

app = FastAPI(
    title='Bill Site',
    description='Data Visualization for bill',
    version='0.0.1'
)


@app.get('/')
async def root():
    return "hello"


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(bill.router, prefix='/bill', tags=['bill'])
