from display.presentation.rest import display
from reception.presentation.rest import reception
from shared_kernel.infra.container import AppContainer
from shared_kernel.infra.database.orm import init_orm_mappers

from fastapi import FastAPI

app_container = AppContainer()

app = FastAPI(
    title="Python-DDD-Hotel",
    contact={"name": "obinata", "email": "k.obinata@karakuri.ai"},
)

app.container = app_container
app.include_router(reception.router)
app.include_router(display.router)


init_orm_mappers()


@app.get("/")
def health_check():
    return {"ping": "pong"}
