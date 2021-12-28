import json
from modules import sql_func
from modules import all_requests


# Находим свободный промокод в базе данных
def find_cod(category_index: int, market_index: int, tg_id: int):
    data_line = sql_func.read_all_3_where(table=f'market_{category_index}_{market_index}',
                                          id_name='status', id_data='active',
                                          id_name2='type_users', id_data2='multicod',
                                          id_name3='type_time', id_data3='simple')
    if str(data_line) == '[]':
        data_cod = '[]'
    else:
        table = data_line[0][1]
        post_id = data_line[0][0]
        data_cod = sql_func.read_all_by_name(table=table, id_name='status', id_data='active')
        if len(data_cod) == 0:
            data_cod = '[]'
            sql_func.update_data(table=f'market_{category_index}_{market_index}', name='status', data='off',
                                 id_name='id', id_data=post_id)
        else:
            id_cod = data_cod[0][0]
            cod = data_cod[0][1]
            new_data_cod = []
            for i in data_line[0]:
                if str(i) == str(table):
                    new_data_cod.append(f'{cod}')
                else:
                    new_data_cod.append(i)
            new_data_cod.append(id_cod)
            sql_func.update_data(table=table, name='status', data=tg_id,
                                 id_name='id', id_data=id_cod)
            data_cod = new_data_cod
    if str(data_cod) == '[]':
        data_cod = sql_func.read_all_3_where(table=f'market_{category_index}_{market_index}',
                                             id_name='status', id_data='active',
                                             id_name2='type_users', id_data2='single',
                                             id_name3='type_time', id_data3='simple')
    if str(data_cod) == '[]':
        data_cod = sql_func.read_all_3_where(table=f'market_{category_index}_{market_index}',
                                             id_name='status', id_data='active',
                                             id_name2='type_users', id_data2='for_all',
                                             id_name3='type_time', id_data3='simple')
    if str(data_cod) == '[]':
        return False
    else:
        if type(data_cod[0]) == int:
            return data_cod
        else:
            return data_cod[0]


# Находим свободный ПРЕМИУМ промокод в базе данных
def find_premium_cod(category_index: int, market_index: int, tg_id: int):
    data_line = sql_func.read_all_3_where(table=f'market_{category_index}_{market_index}',
                                          id_name='status', id_data='active',
                                          id_name2='type_users', id_data2='multicod',
                                          id_name3='type_time', id_data3='premium')
    if str(data_line) == '[]':
        data_cod = '[]'
    else:
        table = data_line[0][1]
        post_id = data_line[0][0]
        data_cod = sql_func.read_all_by_name(table=table, id_name='status', id_data='active')
        if len(data_cod) == 0:
            data_cod = '[]'
            sql_func.update_data(table=f'market_{category_index}_{market_index}', name='status', data='off',
                                 id_name='id', id_data=post_id)
        else:
            id_cod = data_cod[0][0]
            cod = data_cod[0][1]
            new_data_cod = []
            for i in data_line[0]:
                if str(i) == str(table):
                    new_data_cod.append(f'{cod}')
                else:
                    new_data_cod.append(i)
            new_data_cod.append(id_cod)
            sql_func.update_data(table=table, name='status', data=tg_id,
                                 id_name='id', id_data=id_cod)
            data_cod = new_data_cod
    if str(data_cod) == '[]':
        data_cod = sql_func.read_all_3_where(table=f'market_{category_index}_{market_index}',
                                             id_name='status', id_data='active',
                                             id_name2='type_users', id_data2='single',
                                             id_name3='type_time', id_data3='premium')
    if str(data_cod) == '[]':
        data_cod = sql_func.read_all_3_where(table=f'market_{category_index}_{market_index}',
                                             id_name='status', id_data='active',
                                             id_name2='type_users', id_data2='for_all',
                                             id_name3='type_time', id_data3='premium')
    if str(data_cod) == '[]':
        return False
    else:
        if type(data_cod[0]) == int:
            return data_cod
        else:
            return data_cod[0]


# Пользователь получает новый пост
def get_cod(category_index: int, market_index: int, tg_id: int):
    try:
        data_cod = find_cod(category_index=category_index, market_index=market_index, tg_id=tg_id)
        if data_cod:
            favorit_number = int(sql_func.read_all_by_name(table=f'all_categorys', id_name='id',
                                                           id_data=category_index)[0][2])
            sql_func.update_data(table=f'all_categorys', name="favorite", data=favorit_number + 1, id_name='id',
                                 id_data=category_index)
            market_name = all_requests.get_market_name_by_index(category_index=category_index,
                                                                market_index=market_index)
            if data_cod[4] == 'single':
                sql_func.update_data(table=f'market_{category_index}_{market_index}',
                                     id_name='id', id_data=data_cod[0],
                                     name='status', data=tg_id)
                sql_func.first_note(table=f'mycod{tg_id}',
                                    id_name='id_cod', data=f'{category_index}_{market_index}_{data_cod[0]}')
            elif data_cod[4] == 'for_all':
                sql_func.first_note(table=f'mycod{tg_id}',
                                    id_name='id_cod', data=f'{category_index}_{market_index}_{data_cod[0]}')
            elif data_cod[4] == 'multicod':
                sql_func.first_note(table=f'mycod{tg_id}',
                                    id_name='id_cod',
                                    data=f'{category_index}_{market_index}_{data_cod[0]}_{data_cod[8]}')
            return {'cod': data_cod[1],
                    'description': data_cod[2],
                    'market_name': market_name,
                    'cod_id': f'{category_index}_{market_index}_{data_cod[0]}'}
        else:
            return False

    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Пользователь получает новый ПРЕМИУМ пост
def get_premium_cod(category_index: int, market_index: int, tg_id: int):
    try:
        data_cod = find_premium_cod(category_index=category_index, market_index=market_index, tg_id=tg_id)
        if data_cod:
            favorit_number = int(sql_func.read_all_by_name(table=f'all_categorys', id_name='id',
                                                           id_data=category_index)[0][2])
            sql_func.update_data(table=f'all_categorys', name="favorite", data=favorit_number + 1, id_name='id',
                                 id_data=category_index)
            market_name = all_requests.get_market_name_by_index(category_index=category_index,
                                                                market_index=market_index)
            if data_cod[4] == 'single':
                sql_func.update_data(table=f'market_{category_index}_{market_index}',
                                     id_name='id', id_data=data_cod[0],
                                     name='status', data=tg_id)
                sql_func.first_note(table=f'mycod{tg_id}',
                                    id_name='id_cod', data=f'{category_index}_{market_index}_{data_cod[0]}')
            elif data_cod[4] == 'for_all':
                sql_func.first_note(table=f'mycod{tg_id}',
                                    id_name='id_cod', data=f'{category_index}_{market_index}_{data_cod[0]}')
            elif data_cod[4] == 'multicod':
                sql_func.first_note(table=f'mycod{tg_id}',
                                    id_name='id_cod',
                                    data=f'{category_index}_{market_index}_{data_cod[0]}_{data_cod[8]}')
            return {'cod': data_cod[1],
                    'description': data_cod[2],
                    'market_name': market_name}
        else:
            return False

    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Пользователь получает все свои посты
def get_my_all_posts(tg_id: int):
    try:
        data_cods = sql_func.read_all_by_name(table=f'mycod{tg_id}', id_name='status', id_data='active')
        if str(data_cods) == '[]':
            return False
        else:
            my_cod_json = {}
            i = 1

            for one_cod in data_cods:
                category_index = str(one_cod[1]).split('_')[0]
                market_index = str(one_cod[1]).split('_')[1]
                market_name = all_requests.get_market_name_by_index(category_index=int(category_index),
                                                                    market_index=int(market_index))

                check_multi = str(one_cod[1]).split('_')

                if len(check_multi) == 3:
                    cod_id = str(one_cod[1]).split('_')[2]
                    one_cod_data = sql_func.read_all_by_name(table=f'market_{category_index}_{market_index}',
                                                             id_name='id', id_data=cod_id)
                    # проверяем удалил ли админ пост
                    if str(one_cod_data[0][6]).startswith('delete_'):
                        sql_func.delete_line_in_table(table=f'mycod{tg_id}', name='id', data=one_cod[0])
                    else:
                        inform = (one_cod_data[0][1], one_cod_data[0][2], market_name, one_cod[0])
                        my_cod_json[i] = inform
                        i += 1
                else:
                    multi_index = str(one_cod[1]).split('_')[2]
                    # Получаем общий текст описания
                    post_data = sql_func.read_all_by_name(table=f'market_{category_index}_{market_index}',
                                                          id_name='id', id_data=multi_index)[0]

                    cod_id = str(one_cod[1]).split('_')[3]
                    one_cod_data = sql_func.read_all_by_name(
                        table=f'multi_{category_index}_{market_index}_{multi_index}',
                        id_name='id', id_data=cod_id)
                    # проверяем удалил ли админ пост
                    if str(post_data[6]).startswith('delete_'):
                        sql_func.delete_line_in_table(table=f'mycod{tg_id}', name='id', data=one_cod[0])
                    else:
                        inform = (one_cod_data[0][1], post_data[2], market_name, one_cod[0])
                        my_cod_json[i] = inform
                        i += 1

            return json.dumps(my_cod_json)

    except Exception as _ex:
        print('[INFO]', _ex)
        return 'ERROR_user_status'


# Пользователь получает все свои посты
def get_lust_post_id(index: str):
    try:
        all_lines = sql_func.read_all(table=f'market_{index}')
        return len(all_lines)

    except Exception as _ex:
        print('[INFO]', _ex)
        return 'ERROR_user_status'


# Собираем и перебираем в категории все магазины
def transform_post_data_to_json(post: tuple, id_cod: str, market_name: str):
    my_cod_json = {}
    # Передаем id_cod, market_name, cod, description, type_users, multi/single, data, status,
    if str(post[1]).startswith('multi_'):
        inform = (f"{id_cod}", market_name, post[1], post[2], post[3], post[4], post[5], post[6])
    else:
        inform = (f"{id_cod}_{post[0]}", market_name, post[1], post[2], post[3], post[4], post[5], post[6])
    my_cod_json['post_inform'] = inform
    return json.dumps(my_cod_json)


# Получаем пост по cod
def get_post_by_cod(category_index: int, market_index: int, post_index: int):
    try:
        data_post = sql_func.read_all_by_name(table=f'market_{category_index}_{market_index}', id_name='id',
                                              id_data=post_index)
        if data_post != '[]':
            market_name = all_requests.get_market_name_by_index(category_index=category_index,
                                                                market_index=market_index)

            return {'cod': data_post[0][1],
                    'description': data_post[0][2],
                    'market_name': market_name,
                    'cod_id': f'{category_index}_{market_index}_{post_index}'}
        else:
            return False

    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'


# Пользователь получает 10 постов
def get_10_posts_by_index(category_index: int, market_index: int):
    try:
        data_cod = sql_func.read_all_with_sort(table=f'market_{category_index}_{market_index}')
        market_name = all_requests.get_market_name_by_index(category_index=category_index,
                                                            market_index=market_index)
        i = 0
        posts = {}
        for line in data_cod:
            i += 1
            posts[i] = {'cod': line[1],
                        'description': line[2],
                        'market_name': market_name,
                        'cod_id': f'{category_index}_{market_index}_{line[0]}'}
            if i > 10:
                break
        return posts

    except Exception as _ex:
        print('[INFO] cant check user status', _ex)
        return 'ERROR_user_status'
