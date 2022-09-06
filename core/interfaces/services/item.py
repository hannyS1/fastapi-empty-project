from abc import ABC
from typing import List

from core.entities import Item


class IItemService(ABC):
    def get_all(self) -> List[Item]:
        raise NotImplementedError()

