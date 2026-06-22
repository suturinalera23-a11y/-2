from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional

from app.db.db import get_db
from app.db import crud
from app import schemas

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/", response_model=list[schemas.BookResponse])
def read_books(
    category_id: Optional[int] = Query(None, description="Filter by category ID"),
    db: Session = Depends(get_db)
):
    if category_id:
        category = crud.get_category(db, category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        return crud.get_books_by_category(db, category_id)
    return crud.get_books(db)

@router.get("/{book_id}", response_model=schemas.BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.post("/", response_model=schemas.BookResponse, status_code=201)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    category = crud.get_category(db, book.category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return crud.create_book(
        db,
        title=book.title,
        description=book.description,
        price=book.price,
        url=book.url,
        category_id=book.category_id
    )

@router.put("/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    if book.category_id is not None:
        category = crud.get_category(db, book.category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
    
    db_book = crud.update_book(
        db,
        book_id,
        title=book.title,
        description=book.description,
        price=book.price,
        url=book.url,
        category_id=book.category_id
    )
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.delete("/{book_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.delete_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return None
