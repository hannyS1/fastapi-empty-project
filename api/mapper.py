from automapper import mapper

from api.dto.item import ItemCategoryViewDto, ItemViewDto
from core.entities import Item, ItemCategory


def configure_mapping():
    mapper.add(ItemCategory, ItemCategoryViewDto)
    mapper.add(Item, ItemViewDto)
