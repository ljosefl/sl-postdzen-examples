def main():
    import psycopg2
    from pgvector.psycopg2 import Vector

    # Подключение к базе данных PostgreSQL
    conn = psycopg2.connect(
        dbname='your_dbname',
        user='your_username',
        password='your_password',
        host='your_host',
        port='your_port'
    )
    cur = conn.cursor()

    # Создание таблицы для векторных данных
    cur.execute(""\"
    CREATE TABLE if not exists documents (
        id SERIAL PRIMARY KEY,
        vector Vector(256)
    )
    ""\"
    )
    conn.commit()

    # Заполнение таблицы векторами
    cur.execute(""\"
    INSERT INTO documents (vector) VALUES (
        Vector(
            0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 7.0, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8.0, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 8.8, 8.9, 9.0, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, 10.0)
    )
    ""\"
    )
    conn.commit()

    # Получение вектора из таблицы
    cur.execute(""\"
    SELECT vector FROM documents WHERE id = 1
    ""\"
    )
    result = cur.fetchone()
    vector = result[0]
    print(vector)

    # Закрытие соединения
    cur.close()
    conn.close()

if __name__ == '__main__':
    main()