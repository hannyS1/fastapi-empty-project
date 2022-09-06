from core.entities import Item
from core.interfaces.repository.item import IItemRepository
from infrastructure.repository.base import BaseRepository


class ItemRepository(BaseRepository[Item], IItemRepository):
    pass
