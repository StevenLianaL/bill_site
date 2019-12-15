from fastapi import FastAPI

app = FastAPI(
    title='Bill Site',
    description='Data Visualization for bill',
    version='0.0.1'
)


@app.get('/')
async def root():
    return "hello"
