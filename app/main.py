from app.db.db import SessionLocal
from app.db import crud

def main():
    db = SessionLocal()
    
    try:
        # Получаем все категории
        categories = crud.get_categories(db)
        
        print("\n" + "="*60)
        print("📚 КНИГИ ПО КАТЕГОРИЯМ 📚")
        print("="*60 + "\n")
        
        for category in categories:
            print(f"📂 Категория: {category.title}")
            print("-" * 50)
            
            # Получаем книги для этой категории
            books = crud.get_books_by_category(db, category.id)
            
            if books:
                for i, book in enumerate(books, 1):
                    print(f"  {i}. 📖 {book.title}")
                    print(f"     Описание: {book.description}")
                    print(f"     Цена: {book.price:.2f} руб.")
                    if book.url:
                        print(f"     Ссылка: {book.url}")
                    print()
            else:
                print("  Книги в этой категории отсутствуют\n")
            
            print("-" * 50)
            print()
            
        # Общая статистика
        all_books = crud.get_books(db)
        print(f"📊 Всего книг в базе: {len(all_books)}")
        print(f"📊 Всего категорий: {len(categories)}")
        print("\n" + "="*60)
        
    except Exception as e:
        print(f"Ошибка при получении данных: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main()
