from fastapi import APIRouter
from sqlalchemy.orm import Session, joinedload

from config.database import SessionLocal
from core.entities import Item
from infrastructure.repository.item import ItemRepository

item_controller = APIRouter(prefix='/api/items')


@item_controller.get("")
async def get_all():
    # item_repo = ItemRepository()
    # print(item_repo.get_all())
    db: Session = SessionLocal()
    query = db.query(Item).options(
        joinedload(Item)
    )
    print(query)
