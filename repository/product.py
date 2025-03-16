from model.project.product import Product, ProductUid

from abc import ABC, abstractmethod

class ProductRepository(ABC):
    @abstractmethod
    def ReadProductUids() -> list[ProductUid]:
        pass

    @abstractmethod
    def ReadProductByUid(uid: ProductUid) -> Product | None:
        pass

    @abstractmethod
    def ReadProductNameByUid(uid: ProductUid) -> str | None:
        pass

    @abstractmethod
    def ReadProductDescriptionByUid(uid: ProductUid) -> str | None:
        pass

    @abstractmethod
    def ReadProductIsDeprecatedByUid(uid: ProductUid) -> bool | None:
        pass