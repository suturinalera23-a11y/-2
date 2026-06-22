from db.db import SessionLocal, engine, Base
from db import models, crud

def init_db():
    # Создание таблиц
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    try:
        # Добавление категорий
        category1 = crud.create_category(db, "Научная фантастика")
        category2 = crud.create_category(db, "Детективы")
        
        # Добавление книг в первую категорию
        books_data = [
            {"title": "Дюна", "description": "Эпическая научно-фантастическая сага", "price": 899.99},
            {"title": "Основание", "description": "Знаменитая серия о Галактической империи", "price": 749.99},
            {"title": "Звёздный десант", "description": "Классическая военная фантастика", "price": 599.99},
        ]
        
        for book in books_data:
            crud.create_book(
                db,
                title=book["title"],
                description=book["description"],
                price=book["price"],
                category_id=category1.id
            )
        
        # Добавление книг во вторую категорию
        books_data = [
            {"title": "Десять негритят", "description": "Классический детектив Агаты Кристи", "price": 699.99},
            {"title": "Собака Баскервилей", "description": "Знаменитое дело Шерлока Холмса", "price": 549.99},
            {"title": "Убийство в Восточном экспрессе", "description": "Детектив о загадочном убийстве", "price": 649.99},
            {"title": "Имя розы", "description": "Интеллектуальный детектив о средневековом монастыре", "price": 799.99},
        ]
        
        for book in books_data:
            crud.create_book(
                db,
                title=book["title"],
                description=book["description"],
                price=book["price"],
                category_id=category2.id
            )
        
        print("База данных успешно инициализирована!")
        print(f"Создано категорий: 2")
        print(f"Создано книг: 7")
        
    except Exception as e:
        print(f"Ошибка при инициализации: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_db()
