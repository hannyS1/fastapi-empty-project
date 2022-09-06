from typing import List

from pythondi import inject

from core.entities import Item
from core.interfaces.repository.item import IItemRepository
from core.interfaces.services.item import IItemService


class ItemService(IItemService):

    @inject()
    def __init__(self, repository: IItemRepository):
        self.repository = repository

    def get_all(self) -> List[Item]:
        return self.repository.get_all()
