from fastapi import FastAPI
from app.api import books, categories

# Создаём экземпляр приложения
app = FastAPI(
    title="Library API",
    description="API for managing books and categories",
    version="1.0.0"
)

# Подключаем роутеры
app.include_router(books.router)
app.include_router(categories.router)

# Простой эндпоинт для проверки работоспособности
@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "message": "Library API is running"}

# Корневой путь, чтобы не было пусто
@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to Library API!",
        "docs": "/docs",
        "health": "/health"
    }
