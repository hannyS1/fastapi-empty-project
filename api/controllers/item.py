from typing import List

from automapper import mapper
from fastapi import APIRouter

from pythondi import inject

from api.dto.item import ItemViewDto
from core.interfaces.services.item import IItemService

item_controller = APIRouter(prefix='/api/items')


class UseCase:
    @inject()
    def __init__(self, item_service: IItemService):
        self.item_service = item_service


@item_controller.get("")
async def get_all() -> List[ItemViewDto]:
    use_case = UseCase()
    items = use_case.item_service.get_all()

    items_dto = list(map(
        lambda item: mapper.to(ItemViewDto).map(item), items
    ))
    return items_dto
