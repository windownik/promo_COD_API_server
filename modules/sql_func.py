import datetime

import psycopg2
from modules.setings import MainSettings

constant = MainSettings()


def create_db_connect():
    data_base = psycopg2.connect(
        host=constant.db_host(),
        user=constant.user_db(),
        password=constant.password_db(),
        database=constant.db_name()
    )
    return data_base


# Новый юзер создает таблицу в бд
def new_table():
    global data_base
    try:
        data_base = create_db_connect()
        with data_base.cursor() as cursor:
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS all_users (
             id SERIAL PRIMARY KEY,
             tg_id INTEGER UNIQUE,
             user_name TEXT,
             status TEXT DEFAULT 'active',
             activity DATE NOT NULL DEFAULT CURRENT_DATE,
             phone TEXT DEFAULT 'empty',
             first_enter DATE NOT NULL DEFAULT CURRENT_DATE)''')
            data_base.commit()
    except Exception as _ex:
        print('[INFO] Error while working with db', _ex)
    finally:
        if data_base:
            data_base.close()


# Новый юзер создает таблицу в бд
def fast_info_table():
    global data_base
    try:
        data_base = create_db_connect()
        with data_base.cursor() as cursor:
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS fast_info (
             id SERIAL PRIMARY KEY,
             tg_id INTEGER UNIQUE,
             data_1 TEXT,
             data_2 TEXT,
             data_3 TEXT,
             data_4 TEXT,
             data_5 TEXT)''')
            data_base.commit()
    except Exception as _ex:
        print('[INFO] Error while working with db', _ex)
    finally:
        if data_base:
            data_base.close()


# Новый юзер создает таблицу в бд
def new_category_table(index: int):
    global data_base
    try:
        data_base = create_db_connect()
        with data_base.cursor() as cursor:
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS category{index} (
             id SERIAL PRIMARY KEY,
             name TEXT UNIQUE)''')
            data_base.commit()
    except Exception as _ex:
        print('[INFO] Error while working with db', _ex)
    finally:
        if data_base:
            data_base.close()


# Новый юзер создает таблицу в бд
def new_market_table(category_index: int, index: int):
    try:
        db = create_db_connect()
        with db.cursor() as cursor:
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS market_{category_index}_{index} (
             id SERIAL PRIMARY KEY,
             cod TEXT,
             description TEXT,
             type_time TEXT,
             type_users TEXT,
             data DATE NOT NULL DEFAULT CURRENT_DATE,
             status TEXT DEFAULT 'active',
             favorit INTEGER DEFAULT 0
             )''')
            db.commit()
    except Exception as _ex:
        print('[INFO] Error while working with db', _ex)
    finally:
        if db:
            db.close()


# Новый юзер создает таблицу в бд
def all_posts():
    try:
        db = create_db_connect()
        with db.cursor() as cursor:
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS all_posts (
             id SERIAL PRIMARY KEY,
             market_id INTEGER DEFAULT 0,
             cod TEXT,
             description TEXT,
             status TEXT DEFAULT 'active'
             )''')
            db.commit()
    except Exception as _ex:
        print('[INFO] Error while working with db', _ex)
    finally:
        if db:
            db.close()


# Новый юзер создает таблицу в бд
def all_categorys_table():
    global db
    try:
        db = create_db_connect()
        with db.cursor() as cursor:
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS all_categorys (
             id SERIAL PRIMARY KEY,
             name TEXT UNIQUE,
             favorite INTEGER DEFAULT 0
             )''')
            db.commit()
    except Exception as _ex:
        print('[INFO] Error while working with db', _ex)
    finally:
        if db:
            db.close()


# Новый юзер создает таблицу в бд
def report_table():
    global db
    try:
        db = create_db_connect()
        with db.cursor() as cursor:
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS reports (
             id SERIAL PRIMARY KEY,
             cod_id TEXT,
             report_user_id INTEGER,
             report_text TEXT,
             status TEXT DEFAULT 'receive',
             data DATE NOT NULL DEFAULT CURRENT_DATE)''')
            db.commit()
    except Exception as _ex:
        print('[INFO] Error while working with db', _ex)
    finally:
        if db:
            db.close()


# Новый юзер создает таблицу в бд
def my_cod(tg_id: int):
    try:
        db = create_db_connect()
        with db.cursor() as cursor:
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS myCod{tg_id} (
             id SERIAL PRIMARY KEY,
             id_cod TEXT UNIQUE,
             status TEXT DEFAULT 'active')''')
            db.commit()
    except Exception as _ex:
        print('[INFO] Error while working with db', _ex)
    finally:
        if db:
            db.close()


# Создаем таблицу сульти постов
def multipost_table(table_name: str):
    try:
        db = create_db_connect()
        with db.cursor() as cursor:
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} (
             id SERIAL PRIMARY KEY,
             cod TEXT,
             status TEXT DEFAULT 'active')''')
            db.commit()
    except Exception as _ex:
        print('[INFO] Error while working with db', _ex)
    finally:
        if db:
            db.close()


# Новый юзер создает таблицу в бд
def constants():
    global db
    try:
        db = create_db_connect()
        with db.cursor() as cursor:
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS constants (
             id SERIAL PRIMARY KEY,
             chat_moder TEXT UNIQUE)''')
            cursor.execute(f"INSERT INTO constants (chat_moder) VALUES ('https://t.me/sovacode') ON "
                           f"CONFLICT DO NOTHING;")
            db.commit()
    except Exception as _ex:
        print('[INFO] Error while working with db', _ex)
    finally:
        if db:
            db.close()


# Делаем запись новой строки в базу данных
def first_note(table: str, id_name: str, data):
    global db
    try:
        db = create_db_connect()
        with db.cursor() as cursor:
            cursor.execute(f"INSERT INTO {table} ({id_name}) VALUES ('{data}') ON CONFLICT DO NOTHING;")
            db.commit()

    except Exception as _ex:
        print('[INFO] Error while working with db', _ex)
    finally:
        if db:
            db.close()


# Делаем запись новой строки в таблицу репортов
def write_report(cod_id: str, report_user_id: int, report_text: str):
    data = datetime.datetime.now()
    try:
        db = create_db_connect()
        with db.cursor() as cursor:
            cursor.execute(f"INSERT INTO reports (cod_id, report_user_id, report_text, data) "
                           f"VALUES ('{cod_id}', {report_user_id}, '{report_text}', '{data}') ON CONFLICT DO NOTHING;")
            db.commit()

    except Exception as _ex:
        print('[INFO] Error while working with db', _ex)
    finally:
        if db:
            db.close()


# Обновляем данные в базе данных
def update_data(table: str, data, name: str, id_data, id_name: str = 'tg_id'):
    try:
        db = create_db_connect()
        with db.cursor() as cursor:
            cursor.execute(f"UPDATE {table} SET {name}=('{data}') WHERE {id_name}='{id_data}'")
            db.commit()

    except Exception as _ex:
        print('[INFO] Error while working with db', _ex)
    finally:
        if db:
            db.close()


# Делаем запись новой строки в базу данных
def update_user_data(table: str,
                     data,
                     name: str,
                     data2,
                     name2: str,
                     id_data,
                     id_name: str = 'tg_id'):
    try:
        db = create_db_connect()
        with db.cursor() as cursor:
            cursor.execute(f"UPDATE {table} SET {name}=('{data}'),{name2}=('{data2}') WHERE {id_name}='{id_data}'")
            db.commit()

    except Exception as _ex:
        print('[INFO] Error while working with db', _ex)
    finally:
        if db:
            db.close()


# Делаем запись новой строки в базу данных
def update_user_data3(table: str,
                      data,
                      name: str,
                      data2,
                      name2: str,
                      data3,
                      name3: str,
                      data4,
                      name4: str,
                      id_data,
                      id_name: str = 'tg_id'):
    global db
    try:
        db = create_db_connect()
        with db.cursor() as cursor:
            cursor.execute(f"UPDATE {table} SET {name}=('{data}'),"
                           f"{name2}=('{data2}'),{name3}=('{data3}'), {name4}=('{data4}') "
                           f"WHERE {id_name}='{id_data}'")
            db.commit()

    except Exception as _ex:
        print('[INFO] Error while working with db', _ex)
    finally:
        if db:
            db.close()


# Читаем все данные из базы данных
def read_all(
        name: str = '*',
        table: str = 'all_users'):
    global db
    try:

        db = create_db_connect()
        with db.cursor() as cursor:
            cursor.execute(f'SELECT {name} FROM {table}')
            data = cursor.fetchall()
            return data

    except Exception as _ex:
        print('[INFO] Error while working with db', _ex)
    finally:
        if db:
            db.close()


# Собираем все записи с фильтрацией по 1 параметру
def read_all_by_name(
        id_data,
        id_name: str = 'tg_id',
        name: str = '*',
        table: str = 'all_users'):
    global db
    try:

        db = create_db_connect()
        with db.cursor() as cursor:
            cursor.execute(f"SELECT {name} FROM {table} WHERE {id_name}='{id_data}'")
            data = cursor.fetchall()
            return data

    except Exception as _ex:
        print('[INFO] Error while working with db', _ex)
    finally:
        if db:
            db.close()


# Собираем все записи с фильтрацией по 1 параметру и с сортировкой по id
def read_all_with_sort(
        name: str = '*',
        table: str = 'all_users',
        sort_name: str = 'id'):
    global db
    try:

        db = create_db_connect()
        with db.cursor() as cursor:
            cursor.execute(f"SELECT {name} FROM {table} ORDER BY {sort_name} DESC")
            data = cursor.fetchall()
            return data

    except Exception as _ex:
        print('[INFO] Error while working with db', _ex)
    finally:
        if db:
            db.close()


# Собираем все записи с фильтрацией по 1 параметру и с сортировкой по id
def read_all_with_sort_by_data(
        name_date: str,
        data_start: str,
        data_finish: str,
        table: str = 'all_users'):
    global db
    try:

        db = create_db_connect()
        with db.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {table}  WHERE "
                           f"{name_date}::date >= '{data_start}' AND "
                           f"{name_date}::date <= '{data_finish}' ORDER BY id DESC")
            data = cursor.fetchall()
            return data

    except Exception as _ex:
        print('[INFO] Error while working with db', _ex)
    finally:
        if db:
            db.close()


# Собираем все записи с фильтрацией по 3 параметрам
def read_all_3_where(
        id_data,
        id_data2,
        id_data3,
        id_name: str = 'tg_id',
        id_name2: str = 'tg_id',
        id_name3: str = 'tg_id',
        name: str = '*',
        table: str = 'all_users'):
    global db
    try:

        db = create_db_connect()
        with db.cursor() as cursor:
            cursor.execute(f"SELECT {name} FROM {table} WHERE {id_name}='{id_data}' AND {id_name2}='{id_data2}' "
                           f"AND {id_name3}='{id_data3}'")
            data = cursor.fetchall()
            return data

    except Exception as _ex:
        print('[INFO] Error while working with db', _ex)
    finally:
        if db:
            db.close()


# Удаляем строку в таблице
def delete_line_in_table(data, table: str = 'all_categorys', name: str = 'id'):
    global db
    try:
        db = create_db_connect()
        with db.cursor() as cursor:
            cursor.execute(f"DELETE FROM {table} WHERE {name}='{data}'")
            db.commit()

    except Exception as _ex:
        print('[INFO] Error while working with db', _ex)
    finally:
        if db:
            db.close()


# Удаляем таблицу
def delete_table(table: str):
    global db
    try:
        db = create_db_connect()
        with db.cursor() as cursor:
            cursor.execute(f"DROP TABLE IF EXISTS {table}")
            db.commit()

    except Exception as _ex:
        print('[INFO] Error while working with db', _ex)
    finally:
        if db:
            db.close()
