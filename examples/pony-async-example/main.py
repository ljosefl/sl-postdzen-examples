from pony.orm import *
from datetime import datetime

db = Database()

class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    email = Required(str, unique=True)
    created_at = Required(datetime, default=datetime.now)

db.bind(provider='sqlite', filename='users.db', create_db=True)
db.generate_mapping(create_tables=True)

@db_session
def create_user(name, email):
    User(name=name, email=email)

@db_session
def get_users():
    return select(u for u in User)

@db_session
def update_user(user_id, new_name):
    user = User.get(id=user_id)
    if user:
        user.name = new_name

@db_session
def delete_user(user_id):
    user = User.get(id=user_id)
    if user:
        user.delete()

async def async_create_user(name, email):
    await create_user(name, email)

async def async_get_users():
    return await run(select(u for u in User))

async def async_update_user(user_id, new_name):
    await update_user(user_id, new_name)

async def async_delete_user(user_id):
    await delete_user(user_id)

if __name__ == "__main__":
    import asyncio

    # Создание пользователей
    asyncio.run(async_create_user("Alice", "alice@example.com"))
    asyncio.run(async_create_user("Bob", "bob@example.com"))

    # Получение пользователей
    users = asyncio.run(async_get_users())
    for user in users:
        print(f"User: {user.name}, Email: {user.email}")

    # Обновление пользователя
    asyncio.run(async_update_user(1, "Alice Updated"))

    # Получение обновленного пользователя
    users = asyncio.run(async_get_users())
    for user in users:
        print(f"Updated User: {user.name}, Email: {user.email}")

    # Удаление пользователя
    asyncio.run(async_delete_user(2))