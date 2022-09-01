from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional

from sqlalchemy.sql.elements import BooleanClauseList, UnaryExpression

from config.database import Base
from core.interfaces.ipagination import IPagination

T = TypeVar("T", bound=Base)


class ISpecification(ABC):

    @abstractmethod
    def get_criteria(self) -> Optional[BooleanClauseList]:
        raise NotImplementedError()

    @abstractmethod
    def get_order(self) -> Optional[UnaryExpression]:
        raise NotImplementedError()

    @abstractmethod
    def get_pagination(self) -> Optional[IPagination]:
        raise NotImplementedError()
