from abc import ABC, abstractmethod, ABCMeta
from typing import List

from core.entities import Item
from core.interfaces.repository.ibase_repository import IBaseRepository


class IItemRepository(ABC, IBaseRepository[Item]):
    pass
