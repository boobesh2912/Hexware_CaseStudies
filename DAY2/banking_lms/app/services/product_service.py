from sqlalchemy.orm import Session
from app.repositories.product_repository import ProductRepository
from app.exceptions.custom_exceptions import LoanProductNotFoundException

class ProductService:
    def __init__(self, db: Session):
        self.product_repo = ProductRepository(db)

    def create_product(self, product_data: dict):
        return self.product_repo.create_product(product_data)

    def get_product(self, product_id: int):
        product = self.product_repo.get_product_by_id(product_id)
        if not product:
            raise LoanProductNotFoundException(product_id)
        return product

    def get_all_products(self, skip: int = 0, limit: int = 10):
        return self.product_repo.get_all_products(skip, limit)

    def update_product(self, product_id: int, update_data: dict):
        product = self.get_product(product_id)
        return self.product_repo.update_product(product, update_data)

    def delete_product(self, product_id: int):
        product = self.get_product(product_id)
        self.product_repo.delete_product(product)