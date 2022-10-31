from fastapi import FastAPI

from context.display.presentation.rest import display
from context.reception.presentation.rest import reception

app = FastAPI(
    title="Python-DDD-Hotel",
    contact={
        "name": "qu3vipon",
        "email": "qu3vipon@gmail.com",
    },
)


@app.get("/")
def health_check():
    return {"ping": "pong"}


app.include_router(reception.router)
app.include_router(display.router)
