from pythondi import Provider, configure

from core.interfaces.repository.item import IItemRepository
from core.interfaces.services.item import IItemService
from infrastructure.repository.item import ItemRepository
from infrastructure.services.item import ItemService


def configure_dependencies():

    provider = Provider()

    configure(provider)

    provider.bind(IItemRepository, ItemRepository)
    provider.bind(IItemService, ItemService)
