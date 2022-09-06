from pydantic import BaseModel


class ItemCategoryViewDto(BaseModel):
    id: int
    name: str


class ItemViewDto(BaseModel):
    id: int
    name: str
    category: ItemCategoryViewDto
