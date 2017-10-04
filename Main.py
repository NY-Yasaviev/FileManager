import os
import vk

from DataAnalyzer import DataAnalyzer
from DataCollector import DataCollector

session = vk.AuthSession(
    access_token="5a74d7cf875dcbf7c033705e56ee4afa50da8951bd8e131aab2055c076b6e43045f64933690099888e9b4")
cmd = ''
vk_api = vk.API(session)

while not cmd == 'exit':
    cmd = input('Введите команду: ')

    if cmd == 'collect':
        user_id = input('Введите ID пользователя: ')
        time_for_waiting = input('Введите период времени для сканирования(в часах): ')
        data_collector = DataCollector(vk_api)
        data_collector.start_collecting(user_id, time_for_waiting)

    if cmd == 'show':
        user_id = input('Введите ID пользователя: ')
        user_id = vk_api.users.get(user_ids=user_id)[0]['uid']
        user = vk_api.users.get(user_ids=user_id)
        name_id = user[0]['first_name'] + " " + user[0]['last_name']
        if os.path.isfile('data' + str(user_id) + '.json'):
            data_analyzer = DataAnalyzer()
            for data_row in data_analyzer.get_favorites(user_id, name_id):
                print(data_row)
        else:
            print('Для данного пользователя информации нет')

    if cmd == 'likes':
        user_id = input('Введите ID пользователя: ')
        user_id = vk_api.users.get(user_ids=user_id)[0]['uid']
        request_count = int(input('Введите кол-во запросов: '))
        data_analyzer = DataAnalyzer()
        likes = data_analyzer.get_likes(user_id, request_count, vk_api)
        if len(likes) > 0:
            for like in likes:
                print(like)
        else:
            print('Лайки не найдены')
