from typing import TypeVar, Generic, Optional, get_args, List

from sqlalchemy.orm import Query

from config.database import Base, SessionLocal
from core.interfaces.repository.ibase_repository import IBaseRepository
from core.interfaces.specifications.ispecification import ISpecification

T = TypeVar("T", bound=Base)


class BaseRepository(Generic[T]):
    def __init__(self):
        self.db = SessionLocal()
        self.Model = get_args(type(self).__orig_bases__[0])[0]

    def get_base_query(self) -> Query:
        return self.db.query(self.Model)

    def get_all(
            self,
            specification: Optional[ISpecification] = None,
    ) -> List[T]:
        query = self.get_base_query()

        if not specification:
            print(query)
            return query.all()

        if specification.get_criteria() is not None:
            query = query.filter(specification.get_criteria())
        if specification.get_order() is not None:
            query = query.order_by(specification.get_order())
        if specification.get_pagination() is not None:
            parameters = specification.get_pagination().get_parameters()
            query = query.limit(parameters.limit).offset(parameters.offset)

        return query.all()

    def get_by_id(self, pk: int) -> Optional[T]:
        obj: T = self.get_base_query().get(pk)
        return obj

    def create(self, obj: T):
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def bulk_create(self, objs: List[T]) -> List[T]:
        self.db.bulk_save_objects(objs)
        self.db.commit()
        return objs

    def update(self, obj: T):
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def update_many(self, specification: ISpecification, values: dict):
        self.db.query(T).filter(specification.get_criteria()).update(values)

    def get_count(self, specification: ISpecification) -> int:
        return self.get_base_query().filter(specification.get_criteria()).count()

    def __del__(self):
        self.db.close()
