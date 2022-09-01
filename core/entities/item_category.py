from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base


class ItemCategory(Base):
    __tablename__ = "item_category"

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
