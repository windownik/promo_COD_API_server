
from modules import all_requests
from modules.flusk_app import app


# Сохраняем временную информацию 1
@app.route('/data1/<int:tg_id>/<string:data>/')
def save_info_data1(tg_id: int, data: str):
    all_requests.save_data1(tg_id=tg_id, data=data)
    return {"data_1_save": "ok"}


# Сохраняем временную информацию 2
@app.route('/data2/<int:tg_id>/<string:data>/')
def save_info_data2(tg_id: int, data: str):
    all_requests.save_data2(tg_id=tg_id, data=data)
    return {"data_2_save": "ok"}


# Сохраняем временную информацию 3
@app.route('/data3/<int:tg_id>/<string:data>/')
def save_info_data3(tg_id: int, data: str):
    all_requests.save_data3(tg_id=tg_id, data=data)
    return {"data_3_save": "ok"}


# Сохраняем временную информацию 4
@app.route('/data4/<int:tg_id>/<string:data>/')
def save_info_data4(tg_id: int, data: str):
    all_requests.save_data4(tg_id=tg_id, data=data)
    return {"data_4_save": "ok"}


# Сохраняем временную информацию 5
@app.route('/data5/<int:tg_id>/<string:data>/')
def save_info_data5(tg_id: int, data: str):
    all_requests.save_data5(tg_id=tg_id, data=data)
    return {"data_5_save": "ok"}


# Читаем временную информацию 1
@app.route('/data1/read/<int:tg_id>/')
def read_info_data1(tg_id: int):
    data = all_requests.read_data1(tg_id=tg_id)
    return {"data_1": data}


# Читаем временную информацию 2
@app.route('/data2/read/<int:tg_id>/')
def read_info_data2(tg_id: int):
    data = all_requests.read_data2(tg_id=tg_id)
    return {"data_2": data}


# Читаем временную информацию 3
@app.route('/data3/read/<int:tg_id>/')
def read_info_data3(tg_id: int):
    data = all_requests.read_data3(tg_id=tg_id)
    return {"data_3": data}


# Читаем временную информацию 4
@app.route('/data4/read/<int:tg_id>/')
def read_info_data4(tg_id: int):
    data = all_requests.read_data4(tg_id=tg_id)
    return {"data_4": data}


# Читаем временную информацию 5
@app.route('/data5/read/<int:tg_id>/')
def read_info_data5(tg_id: int):
    data = all_requests.read_data5(tg_id=tg_id)
    return {"data_5": data}
