from fastapi import FastAPI

from api.controllers.item import item_controller
from api.dependencies import configure_dependencies
from api.mapper import configure_mapping

app = FastAPI(
    docs_url='/docs',
)

app.include_router(item_controller)


@app.on_event("startup")
async def startup():
    configure_dependencies()
    configure_mapping()
