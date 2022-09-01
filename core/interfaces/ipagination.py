from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class PaginationParam:
    limit: int
    offset: int


class IPagination(ABC):

    @abstractmethod
    def get_parameters(self) -> PaginationParam:
        pass
