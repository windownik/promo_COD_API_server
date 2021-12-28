from modules import all_requests, find_get_cod
from modules.flusk_app import app


# Create all tables
@app.route('/init/')
def create_tables():
    return all_requests.create_db()


# create new user in table all_users
@app.route('/new_user/<int:tg_id>/<string:name>/')
def create_new_user(tg_id: int, name: str):
    return all_requests.create_new_user(tg_id, name)


# create new admin
@app.route('/new_admin/<int:tg_id>/')
def create_new_admin(tg_id: int):
    return all_requests.new_status(tg_id, status='admin')


# delete admin
@app.route('/delete_admin/<int:tg_id>/')
def delete_admin(tg_id: int):
    return all_requests.new_status(tg_id, status='active')


# delete admin
@app.route('/ban_user/<int:tg_id>/')
def ban_user(tg_id: int):
    return all_requests.new_status(tg_id, status='ban')


# Check status user
@app.route('/is_admin_user/<int:tg_id>/')
def check_admin(tg_id: int):
    return all_requests.is_admin(tg_id)


# Check status user
@app.route('/save_phone/<int:tg_id>/<string:phone>/')
def save_phone(tg_id: int, phone: str):
    return all_requests.save_phone(tg_id=tg_id, phone=phone)


# Check premium status user
@app.route('/is_user_premium/<int:tg_id>/')
def check_user_phone(tg_id: int):
    return all_requests.check_user_phone(tg_id)


# Get all category
@app.route('/categorys/')
def get_all_categorys():
    data = all_requests.get_category()
    if data:
        return data
    else:
        return {"category": False}


# Get category by index
@app.route('/category/<string:index>/')
def get_category_by_index(index):
    data = all_requests.get_category_by_index(index)
    if data:
        return {"name": data}
    else:
        return {"category": False}


# Get category by index
@app.route('/category/market_name/<int:category_index>/<int:market_index>/')
def get_market_name_by_index(category_index: int, market_index: int):
    data = all_requests.get_market_name_by_index(category_index=category_index, market_index=market_index)
    if data:
        return {"name": data}
    else:
        return {"category": False}


# Get category by index
@app.route('/category/delete_market/<int:category_index>/<int:market_index>/')
def delete_market(category_index: int, market_index: int):
    data = all_requests.delete_market(category_index=category_index, market_index=market_index)
    if data:
        return {"name": data}
    else:
        return {"category": False}


# Rename market
@app.route('/category/rename_market/<int:category_index>/<int:market_index>/<string:name>/')
def correct_market_name(category_index: int, market_index: int, name: str):
    data = all_requests.new_market_name(category_index=category_index, market_index=market_index, name=name)
    if data:
        return {"name": data}
    else:
        return {"category": False}


# Create new Category
@app.route('/categorys/create/<string:name>/')
def create_category(name: str):
    all_requests.create_category(name=name)
    return {"new_category": "ok"}


# Delete new Category
@app.route('/categorys/delete/<int:index>/')
def delete_category(index: int):
    all_requests.delete_category(index=index)
    return {"delete_category": "ok"}


# Get all category
@app.route('/sub_categorys/<int:index>/')
def get_all_subcategorys(index):
    data = all_requests.get_sub_category(index=index)
    if data:
        return data
    else:
        return {"sub_category": False}


# Меняем имя категории
@app.route('/category_correct/<int:index>/<string:name>/')
def new_category_name(index: int, name: str):
    all_requests.new_category_name(index=index, name=name)
    return {"correct": "ok"}


# Create new SUB Category
@app.route('/create_sub_category/<string:name>/<int:index>/')
def create_sub_category(name: str, index: int):
    all_requests.create_sub_category(name=name, index=index)
    return {"new_category": "ok"}


# Создаем новый пост
@app.route('/save_new_post/<string:index>/<string:cod>/<string:description>/<string:type_time>/<string:type_users>/')
def save_new_post(index: str, cod: str, description: str, type_time: str, type_users: str):
    all_requests.create_new_post(index=index,
                                 cod=cod,
                                 description=description,
                                 type_time=type_time,
                                 type_users=type_users)
    return {"new_post": "ok"}


# Создаем новый пост
@app.route('/get_post/<string:call_data>/<int:tg_id>/')
def get_post(call_data: str, tg_id: int):
    category_index = str(call_data).split('_')[1]
    market_index = str(call_data).split('_')[2]
    promocod = find_get_cod.get_cod(category_index=int(category_index), market_index=int(market_index), tg_id=tg_id)
    if promocod:
        return promocod
    else:
        return {"no_cod": "ok"}


# Создаем новый пост
@app.route('/get_premium_post/<string:call_data>/<int:tg_id>/')
def get_premium_post(call_data: str, tg_id: int):
    category_index = str(call_data).split('_')[1]
    market_index = str(call_data).split('_')[2]
    promocod = find_get_cod.get_premium_cod(category_index=int(category_index), market_index=int(market_index),
                                            tg_id=tg_id)
    if promocod:
        return promocod
    else:
        return {"no_cod": "ok"}


# Получаем 10 последних постов
@app.route('/get_10_posts_by_index/<string:category_index>/<string:market_index>/')
def get_10_posts_by_index(category_index: str, market_index: str):
    promocod = find_get_cod.get_10_posts_by_index(category_index=int(category_index), market_index=int(market_index))
    if promocod:
        return promocod
    else:
        return {"no_cod": "ok"}


# Создаем новый пост
@app.route('/get_post/by_index/<string:cod>/')
def get_post_by_index(cod: str):
    category_index = str(cod).split('_')[0]
    market_index = str(cod).split('_')[1]
    post_index = str(cod).split('_')[2]

    promocod = find_get_cod.get_post_by_cod(category_index=int(category_index), market_index=int(market_index),
                                            post_index=int(post_index))
    if promocod:
        return promocod
    else:
        return {"no_cod": "ok"}


# Получаем все посты из избранного
@app.route('/get_my_post/<int:tg_id>/')
def get_my_posts(tg_id: int):
    my_posts = find_get_cod.get_my_all_posts(tg_id)
    if my_posts:
        return my_posts
    else:
        return {"no_posts": "ok"}


# Получаем id номер последнего предложения в базеданных
@app.route('/get_lust_post_id/<string:index>/')
def get_lust_post_id(index: str):
    number_of_posts = find_get_cod.get_lust_post_id(index)
    if number_of_posts:
        return {"number_posts": number_of_posts}
    else:
        return {"number_posts": False}


# Получаем все посты из избранного
@app.route('/delete_my_post/<int:tg_id>/<string:post_data>/')
def delete_my_post(tg_id: int, post_data: str):
    my_posts = all_requests.delete_my_post(tg_id=tg_id, post_data=post_data)
    if my_posts:
        return my_posts
    else:
        return {"no_posts": "ok"}


# Отправляем жалобу
@app.route('/send_report/<string:report_text>/<int:tg_id>/')
def send_report(tg_id: int, report_text: str):
    post_cod = all_requests.read_data1(tg_id=tg_id)
    report_feed_back = all_requests.send_report(tg_id=tg_id, report_text=report_text, post_cod=post_cod)
    if report_feed_back:
        return {"send_report": "ok"}
    else:
        return {"send_report": "no"}


# Get category by index
@app.route('/moder_chat/get/')
def get_moder_chat():
    data = all_requests.get_moder_chat()
    if data:
        return {"chat": data}
    else:
        return {"no_chat": False}


# Get category by index
@app.route('/send_chat_id/<string:chat_id>/')
def send_new_chat(chat_id: str):
    data = all_requests.send_new_chat_chat(chat_id)
    if data:
        return {"new_chat": data}
    else:
        return {"new_chat": False}


# Get category by index
@app.route('/find_user/<string:text>/')
def find_user(text: str):
    data = all_requests.find_user_in_db(text)
    if data:
        return {"find_user": data}
    else:
        return {"find_user": False}


# Create new table in db
@app.route('/creat_new_table/<string:table_name>/')
def creat_new_table(table_name: str):
    data = all_requests.create_multipost_table(table_name)
    if data:
        return {"create_table": True}
    else:
        return {"create_table": False}


# Create new table in db
@app.route('/save_multipost_cod/<string:table_name>/<string:cod>/')
def save_multipost(table_name: str, cod: str):
    data = all_requests.save_multipost_cod(table_name, cod)
    if data:
        return {"save_cod": True}
    else:
        return {"save_cod": False}


# Create new table in db
@app.route('/search_post_by_cod/<string:cod>/')
def search_post_by_cod(cod: str):
    data = all_requests.search_post_by_cod(cod)
    return data


# Update post description
@app.route('/update_post_description/<string:cod>/<string:description>/')
def update_post_description(cod: str, description: str):
    data = all_requests.update_post_description(cod=cod, description=description)
    return data


# Update post status
@app.route('/update_post_status/<string:cod>/<string:status>/')
def update_post_status(cod: str, status: str):
    data = all_requests.update_post_status(cod=cod, status=status)
    return data


# Update post status
@app.route('/get_users_statistic/')
def get_users_statistic():
    data = all_requests.get_users_statistic()
    return data


# Update post status
@app.route('/get_bad_cod_statistic/')
def get_bad_cod_statistic():
    data = all_requests.get_bad_cod_statistic()
    return data


# Update post status
@app.route('/get_top_categorys/')
def get_top_categorys():
    data = all_requests.get_top_categorys()
    return data
