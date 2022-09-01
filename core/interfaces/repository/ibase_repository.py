from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional

from config.database import Base
from core.interfaces.specifications.ispecification import ISpecification

T = TypeVar("T", bound=Base)


class IBaseRepository(Generic[T], ABC):

    @abstractmethod
    def get_all(
            self,
            specification: Optional[ISpecification] = None,
    ) -> List[T]:
        raise NotImplementedError()

    @abstractmethod
    def get_by_id(self, pk: int) -> Optional[T]:
        raise NotImplementedError()

    @abstractmethod
    def create(self, obj: T):
        raise NotImplementedError()

    @abstractmethod
    def bulk_create(self, objs: List[T]):
        raise NotImplementedError()

    @abstractmethod
    def update(self, obj: T):
        raise NotImplementedError()

    @abstractmethod
    def update_many(self, specification: ISpecification, values: dict):
        raise NotImplementedError()

    @abstractmethod
    def get_count(self, specification: Optional[ISpecification]) -> int:
        raise NotImplementedError()
