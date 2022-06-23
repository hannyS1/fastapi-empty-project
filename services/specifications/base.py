from sqlalchemy import or_, and_, not_

from dataclasses import dataclass
from sqlalchemy.sql.elements import BooleanClauseList

from abc import ABC, abstractmethod


class BaseSpecification(ABC):

    @abstractmethod
    def get_criteria(self) -> BooleanClauseList:
        raise NotImplementedError()

    def And(self, other: "BaseSpecification") -> "AndSpecification":
        return AndSpecification(self, other)

    def Or(self, other: "BaseSpecification") -> "OrSpecification":
        return OrSpecification(self, other)

    def Not(self) -> "NotSpecification":
        return NotSpecification(self)


@dataclass(frozen=True)
class AndSpecification(BaseSpecification):
    first: BaseSpecification
    second: BaseSpecification

    def get_criteria(self) -> BooleanClauseList:
        return and_(self.first.get_criteria(), self.second.get_criteria())


@dataclass(frozen=True)
class OrSpecification(BaseSpecification):
    first: BaseSpecification
    second: BaseSpecification

    def get_criteria(self) -> BooleanClauseList:
        return or_(self.first.get_criteria(), self.second.get_criteria())


@dataclass(frozen=True)
class NotSpecification(BaseSpecification):
    subject: BaseSpecification

    def get_criteria(self) -> BooleanClauseList:
        return not_(self.subject.get_criteria())
