from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.services.product_service import ProductService
from app.schemas.product_schema import LoanProductCreate, LoanProductUpdate, LoanProductResponse

router = APIRouter(prefix="/loan-products", tags=["Loan Products"])

@router.post("/", response_model=LoanProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product_data: LoanProductCreate, db: Session = Depends(get_db)):
    return ProductService(db).create_product(product_data.model_dump())

@router.get("/", response_model=List[LoanProductResponse])
def get_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return ProductService(db).get_all_products(skip, limit)

@router.get("/{product_id}", response_model=LoanProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return ProductService(db).get_product(product_id)

@router.put("/{product_id}", response_model=LoanProductResponse)
def update_product(product_id: int, product_data: LoanProductUpdate, db: Session = Depends(get_db)):
    return ProductService(db).update_product(product_id, product_data.model_dump())

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    ProductService(db).delete_product(product_id)