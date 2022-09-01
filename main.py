from fastapi import FastAPI

from api.controllers.item import item_controller

app = FastAPI(
    docs_url='/docs',
)

app.include_router(item_controller)
