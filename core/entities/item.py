from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    category_id = Column(ForeignKey("item_category.id", ondelete="CASCADE"))

    category = relationship("ItemCategory")
