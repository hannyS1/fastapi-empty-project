from typing import Optional, TypeVar, Generic, Type

from sqlalchemy.sql.elements import UnaryExpression, BooleanClauseList

from config.database import Base
from core.entities import Item
from core.interfaces.ipagination import IPagination
from core.interfaces.specifications.ispecification import ISpecification


T = TypeVar("T", bound=Base)


class BaseSpecification(Generic[T], ISpecification):

    __order: UnaryExpression
    __pagination: IPagination

    def __init__(
            self,
            criteria: Optional[BooleanClauseList] = None,
    ):
        self.__criteria = criteria

    def get_criteria(self) -> Optional[BooleanClauseList]:
        return self.__criteria

    def get_order(self) -> Optional[UnaryExpression]:
        return self.__order

    def get_pagination(self) -> Optional[IPagination]:
        return self.__pagination

    @classmethod
    def add_order(cls, order: UnaryExpression):
        cls.__order = order

    @classmethod
    def add_pagination(cls, pagination: IPagination):
        cls.__pagination = pagination
