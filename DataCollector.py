import vk, os, time, json


class DataCollector:
    def __init__(self, vk_api):
        self.vk_api = vk_api

    def start_collecting(self, user_id, t_for_w=1, buffer_size=1):
        friends = {}

        user_id = self.vk_api.users.get(user_ids=user_id)[0]['uid']

        time_to_stop = time.time() + float(t_for_w) * 60 * 60

        write_marker = 0

        while time.time() < time_to_stop:
            try:
                t = int(time.time())
                for friend in self.vk_api.friends.get(user_id=user_id, fields='online'):
                    name_id = friend['first_name'] + " " + friend['last_name']
                    is_online = friend['online']
                    try:
                        friends[name_id].update({t: is_online})
                    except KeyError:
                        friends[name_id] = {t: is_online}

                time.sleep(0.5)
                user = self.vk_api.users.get(fields='online')
                is_online = user[0]['online']
                name_id = user[0]['first_name'] + " " + user[0]['last_name']
                try:
                    friends[name_id].update({t: is_online})
                except KeyError:
                    friends[name_id] = {t: is_online}

                write_marker += 1
                if write_marker % buffer_size == 0:
                    if os.path.isfile('data' + str(user_id) + '.json'):
                        with open('data' + str(user_id) + '.json', "r", encoding="utf-8") as file:
                            friends_from_json = json.load(file)
                            for key, value in friends_from_json.items():
                                value.update(friends[key])
                    else:
                        friends_from_json = friends

                    with open('data' + str(user_id) + '.json', "w", encoding="utf-8") as file:
                        json.dump(friends_from_json, file)
            except:
                pass

            time.sleep(59.5)
