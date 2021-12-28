import datetime
from modules import sql_func
from modules.data_functions import data_to_json
from modules.find_get_cod import transform_post_data_to_json


# Создаем базу данных
def create_db():
    try:
        sql_func.new_table()
        sql_func.fast_info_table()
        sql_func.all_categorys_table()
        # sql_func.all_posts()
        sql_func.report_table()
        sql_func.constants()
        return {'ok': 'create_db'}
    except Exception as _ex:
        print('[INFO] cant create new table', _ex)
        return 'ERROR in DB'


# Добавляем нового пользователя в бд
def create_new_user(tg_id: int, name: str):
    try:
        user_data = sql_func.read_all_by_name(id_data=tg_id)
        if str(user_data) == '[]':
            sql_func.my_cod(tg_id=tg_id)
            sql_func.first_note(table='all_users', id_name='tg_id', data=tg_id)
        sql_func.update_user_data(table='all_users', name='user_name', name2='activity',
                                  data2=datetime.datetime.now(), data=name, id_data=tg_id)
        return {'ok': 'create_user'}
    except Exception as _ex:
        print('[INFO] cant create new user', _ex)
        return 'ERROR in DB'


# Меняем статус пользователя
def new_status(tg_id: int, status: str):
    try:
        sql_func.update_data(table='all_users', name='status', data=status, id_data=tg_id)
        return {'new_status': status}
    except Exception as _ex:
        print('[INFO] cant create new user', _ex)
        return 'ERROR in DB'


# Возращаем статус
def user_status(tg_id: int):
    try:
        user_status = sql_func.read_all_by_name(id_data=tg_id, name='status')[0][0]
        return user_status
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Проверяем админ ли пользователь
def is_admin(tg_id: int):
    status = user_status(tg_id)
    if status == "admin":
        return {'admin': True}
    else:
        return {'admin': False}


# Меняем статус пользователя на премиум
def save_phone(tg_id: int, phone: str):
    try:
        sql_func.update_data(table='all_users', name='phone', data=phone, id_data=tg_id)
        return {'phone': True}
    except Exception as _ex:
        print('[INFO] cant create new user', _ex)
        return 'ERROR in DB'


# Возращаем статус
def user_phone(tg_id: int):
    try:
        user_status = sql_func.read_all_by_name(id_data=tg_id, name='phone')[0][0]
        return user_status
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Проверяем админ ли пользователь
def check_user_phone(tg_id: int):
    status = user_phone(tg_id)
    if status == "empty":
        return {'premium': False}
    else:
        return {'premium': status}


# Получаем все категории
def get_category():
    try:
        all_categorys = sql_func.read_all(table='all_categorys')
        if str(all_categorys) == '[]':
            return False
        else:
            return data_to_json(all_categorys)
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Получаем все категории
def get_sub_category(index: int):
    try:
        all_categorys = sql_func.read_all(table=f'category{index}')
        if str(all_categorys) == '[]':
            return False
        else:
            return data_to_json(all_categorys)
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Создаем категорию
def create_category(name: str):
    try:
        sql_func.first_note(table='all_categorys', id_name='name', data=name)
        category_index = sql_func.read_all_by_name(table='all_categorys', id_name='name', id_data=name)[0][0]
        sql_func.new_category_table(category_index)
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Удаляем категорию
def delete_category(index: int):
    try:
        sql_func.delete_line_in_table(data=index)
        sql_func.delete_table(table=f"category{index}")
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Определяем описание категории по индексу
def get_category_by_index(index: int):
    try:
        category_index = sql_func.read_all_by_name(table='all_categorys', id_name='id', id_data=index)[0][1]
        return category_index
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Определяем описание категории по индексу
def get_market_name_by_index(category_index: int, market_index: int):
    try:
        category_name = sql_func.read_all_by_name(table=f'category{category_index}', id_name='id',
                                                  id_data=market_index)[0][1]
        return category_name
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Удаляем магазин из категории
def delete_market(category_index: int, market_index: int):
    try:
        sql_func.delete_line_in_table(data=market_index, table=f'category{category_index}')
        sql_func.delete_table(table=f"market_{category_index}_{market_index}")
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Сохраняем временную информацию 1
def save_data1(tg_id: int, data: str):
    try:
        sql_func.first_note(table='fast_info', id_name='tg_id', data=tg_id)
        sql_func.update_data(table='fast_info', name='data_1', data=data, id_data=tg_id)
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Сохраняем временную информацию 2
def save_data2(tg_id: int, data: str):
    try:
        sql_func.first_note(table='fast_info', id_name='tg_id', data=tg_id)
        sql_func.update_data(table='fast_info', name='data_2', data=data, id_data=tg_id)
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Сохраняем временную информацию 3
def save_data3(tg_id: int, data: str):
    try:
        sql_func.first_note(table='fast_info', id_name='tg_id', data=tg_id)
        sql_func.update_data(table='fast_info', name='data_3', data=data, id_data=tg_id)
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Сохраняем временную информацию 4
def save_data4(tg_id: int, data: str):
    try:
        sql_func.first_note(table='fast_info', id_name='tg_id', data=tg_id)
        sql_func.update_data(table='fast_info', name='data_4', data=data, id_data=tg_id)
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Сохраняем временную информацию 5
def save_data5(tg_id: int, data: str):
    try:
        sql_func.first_note(table='fast_info', id_name='tg_id', data=tg_id)
        sql_func.update_data(table='fast_info', name='data_5', data=data, id_data=tg_id)
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Читаем информацию из Data1
def read_data1(tg_id: int):
    try:
        data = sql_func.read_all_by_name(table='fast_info', id_data=tg_id)[0][2]
        return data
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Читаем информацию из Data2
def read_data2(tg_id: int):
    try:
        data = sql_func.read_all_by_name(table='fast_info', id_data=tg_id)[0][3]
        return data
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Читаем информацию из Data3
def read_data3(tg_id: int):
    try:
        data = sql_func.read_all_by_name(table='fast_info', id_data=tg_id)[0][4]
        return data
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Читаем информацию из Data4
def read_data4(tg_id: int):
    try:
        data = sql_func.read_all_by_name(table='fast_info', id_data=tg_id)[0][5]
        return data
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Читаем информацию из Data5
def read_data5(tg_id: int):
    try:
        data = sql_func.read_all_by_name(table='fast_info', id_data=tg_id)[0][6]
        return data
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Меняем название категории
def new_category_name(index: int, name: str):
    try:
        sql_func.update_data(table='all_categorys', name='name', data=name, id_name='id', id_data=index)
        return {'new_name': 'ок'}
    except Exception as _ex:
        print('[INFO] cant create new user', _ex)
        return 'ERROR in DB'


# Меняем название магазина
def new_market_name(category_index: int, market_index: int, name: str):
    try:
        sql_func.update_data(table=f'category{category_index}', name='name', data=name, id_name='id',
                             id_data=market_index)
        return {'new_name': 'ок'}
    except Exception as _ex:
        print('[INFO] cant create new user', _ex)
        return 'ERROR in DB'


# Создаем под категорию категорию
def create_sub_category(name: str, index: int):
    try:
        sql_func.first_note(table=f'category{index}', id_name='name', data=name)
        category_index = sql_func.read_all_by_name(table=f'category{index}', id_name='name', id_data=name)[0][0]
        sql_func.new_market_table(category_index=index, index=category_index)
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Создаем новый пост
def create_new_post(index: str,
                    cod: str,
                    description: str,
                    type_time: str,
                    type_users: str):
    try:
        sql_func.first_note(table=f'market_{index}', id_name='cod', data=cod)
        sql_func.update_user_data3(table=f'market_{index}',
                                   name="description", data=description,
                                   name2='type_time', data2=type_time,
                                   name3='type_users', data3=type_users,
                                   name4='data', data4=datetime.datetime.now(),
                                   id_name='cod', id_data=cod)

    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Создаем новый пост
def delete_my_post(tg_id: int, post_data: str):
    try:
        sql_func.delete_line_in_table(table=f'mycod{tg_id}',
                                      name="id", data=post_data)

    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Создаем новый пост
def send_report(tg_id: int, report_text: str, post_cod: str):
    try:
        sql_func.write_report(cod_id=post_cod, report_user_id=tg_id, report_text=report_text)
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Определяем описание категории по индексу
def get_moder_chat():
    try:
        category_index = sql_func.read_all(table='constants')[0][1]
        return category_index
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Определяем описание категории по индексу
def send_new_chat_chat(chat_id: str):
    try:
        sql_func.update_data(table='constants', name="chat_moder", data=chat_id, id_name='id', id_data=1)
        return 'ok'
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Ищем пользователя в базе данных
def find_user_in_db(text: str):
    try:
        user_data = sql_func.read_all_by_name(table='all_users', id_name='tg_id', id_data=text)
        if str(user_data) == '[]' or user_data is None:
            pass
        else:
            return user_data[0]
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)

    try:
        user_data = sql_func.read_all_by_name(table='all_users', id_name='phone', id_data=text)
        if str(user_data) == '[]':
            return False
        else:
            return user_data[0]
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)


# Определяем описание категории по индексу
def create_multipost_table(table_name: str):
    try:
        sql_func.multipost_table(table_name=table_name)
        return 'ok'
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Определяем описание категории по индексу
def save_multipost_cod(table_name: str, cod: str):
    try:
        sql_func.first_note(table=table_name, id_name='cod', data=cod)
        return 'ok'
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Обновляем описание поста по коду
def update_post_description(cod: str, description: str):
    category = cod.split('_')[0]
    market = cod.split('_')[1]
    post_id = cod.split('_')[2]
    try:
        sql_func.update_data(table=f'market_{category}_{market}', name='description', data=description, id_name='id',
                             id_data=post_id)
        return 'ok'
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Обновляем описание поста по коду
def update_post_status(cod: str, status: str):
    category = cod.split('_')[0]
    market = cod.split('_')[1]
    post_id = cod.split('_')[2]
    try:
        sql_func.update_data(table=f'market_{category}_{market}', name='status', data=status, id_name='id',
                             id_data=post_id)
        return 'ok'
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Определяем описание категории по индексу
def search_post_by_cod(cod_from_user: str):
    try:
        # собираем все активные категории
        all_categorys = sql_func.read_all(table='all_categorys')
        for category in all_categorys:
            # Работаем в нутри одной категории получаем магазины
            category_index = category[0]
            markets = sql_func.read_all(table=f'category{category_index}')
            for market in markets:
                # Работаем в нутри одного магазина собираем все посты
                market_index = market[0]
                market_posts = sql_func.read_all(table=f'market_{category_index}_{market_index}')
                for post in market_posts:
                    # проверяем мульти код
                    if str(post[1]).startswith('multi_'):
                        # Получаем мульти коды
                        id_multicod = post[0]
                        multi_cods = sql_func.read_all(table=f'multi_{category_index}_{market_index}_{id_multicod}')
                        for cod in multi_cods:
                            if str(cod[1]) == str(cod_from_user):
                                market_name = get_market_name_by_index(category_index=category_index,
                                                                       market_index=market_index)
                                inform = transform_post_data_to_json(id_cod=f'{category_index}_{market_index}_'
                                                                            f'{id_multicod}',
                                                                     post=post,
                                                                     market_name=market_name)
                                return inform
                            else:
                                pass
                    # если нашли совпадение
                    elif str(post[1]) == str(cod_from_user):
                        market_name = get_market_name_by_index(category_index=category_index, market_index=market_index)
                        inform = transform_post_data_to_json(id_cod=f'{category_index}_{market_index}', post=post,
                                                             market_name=market_name)
                        return inform
                    else:
                        pass
        return {'post_inform': False}
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Получаем статистику об пользователях
def get_users_statistic():
    try:
        all_users_number = sql_func.read_all_with_sort()[0][0]
        now = str(datetime.datetime.now()).split(' ')[0]
        days_30_early = str(datetime.datetime.now() - datetime.timedelta(days=30)).split(' ')[0]
        all_new_users_number = sql_func.read_all_with_sort_by_data(name_date='first_enter',
                                                                   data_start=days_30_early,
                                                                   data_finish=now)
        active_users_number = sql_func.read_all_with_sort_by_data(name_date='activity',
                                                                  data_start=days_30_early,
                                                                  data_finish=now)

        return {'all_users_number': all_users_number,
                'all_new_users_number': len(all_new_users_number),
                'active_users_number': len(active_users_number)}
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Получаем статистику об репортах
def get_bad_cod_statistic():
    try:
        all_reports_number = sql_func.read_all_with_sort(table='reports')[0][0]
        now = str(datetime.datetime.now()).split(' ')[0]
        days_30_early = str(datetime.datetime.now() - datetime.timedelta(days=30)).split(' ')[0]
        all_new_reports = sql_func.read_all_with_sort_by_data(table='reports',
                                                              name_date='data',
                                                              data_start=days_30_early,
                                                              data_finish=now)

        return {'all_reports_number': all_reports_number,
                'all_new_reports': len(all_new_reports)}
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Получаем статистику об пользователях
def get_top_categorys():
    try:
        favorite_category = sql_func.read_all_with_sort(table='all_categorys', sort_name='favorite')
        return {'favorite_category': favorite_category}
    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'
