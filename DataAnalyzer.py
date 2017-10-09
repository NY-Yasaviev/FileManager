import vk, os, json, time

class DataAnalyzer:
    def __init__(self):
        pass


    def get_favorites(self, user_id, name_id):
        with open('data' + str(user_id) + '.json', "r", encoding="utf-8") as file:
            friends = json.load(file)

            def makeIO(friends):
                for name, fields in friends.items():
                    k = 0
                    for t, online in fields.items():
                        if k == 1 and online == 0:
                            fields[prevT] = 3
                        if k == 0 and online == 1:
                            fields[t] = 2
                        k = online
                        prevT = t
                i = 3
                user_online_past = [0, 0, 0, 0, 0]
                user_time_past = [0, 0, 0, 0, 0]
                friend_talk_list = []
                for user_time, user_online in friends[name_id].items():
                    user_time_past.pop(0)
                    user_time_past.append(user_time)
                    user_online_past.pop(0)
                    user_online_past.append(user_online)
                    i -= 1;

                    if i < 0:
                        for friend_name, friend_fields in friends.items():
                            if not friend_name == name_id:
                                if friend_fields[user_time_past[3]] == user_online_past[3] == 1:
                                    friend_fields[user_time_past[3]] = 4
                                try:
                                    if friend_fields[user_time_past[3]] == 2 and user_online_past.index(2):
                                        friend_fields[user_time_past[3]] = 5
                                        friend_talk_list.append(friend_name)
                                except ValueError:
                                    pass

                                try:
                                    if friend_fields[user_time_past[3]] == 3 and user_online_past.index(3):
                                        if friend_name in friend_talk_list:
                                            friend_fields[user_time_past[3]] = 7
                                        else:
                                            friend_fields[user_time_past[3]] = 6

                                        friend_talk_list.remove(friend_name)
                                    else:
                                        if friend_fields[user_time_past[3]] == 3:
                                            friend_talk_list.remove(friend_name)
                                except ValueError:
                                    pass

            makeIO(friends)

            list_of_lovers = {}
            s = 0
            sBig = 0
            for friend, data in friends.items():
                if not friend == name_id:
                    for t, o in data.items():
                        if o == 4:
                            s += 0.05
                        if o == 5 or o == 6:
                            s += 1
                    sBig += s
                    list_of_lovers.update({friend: s})

            if sBig == 0:
                sBig = 1
            for lover, val in list_of_lovers.items():
                list_of_lovers[lover] = val / sBig * 100

            list_of_lovers = sorted(list_of_lovers.items(), key=lambda x: x[1], reverse=True)

            return list_of_lovers

    def get_likes(self,user_id, cnt, vk_api):
        subscriptions_list = vk_api.users.getSubscriptions(user_id=user_id, extended=0)['groups']['items']
        groups_list = []
        for group in subscriptions_list:
            groups_list.append('-' + str(group))
        posts = {}
        newsfeed = vk_api.newsfeed.get(filters='post', source_ids=', '.join(groups_list), count=100, timeout=10)
        for news in newsfeed['items']:
            posts.update({news['post_id']: news['source_id']})
        for c in range(cnt - 1):
            next_from = newsfeed['new_from']
            newsfeed = vk_api.newsfeed.get(form=next_from, filters='post', source_ids=', '.join(groups_list), count=100, timeout=10)
            for news in newsfeed['items']:
                posts.update({news['post_id']: news['source_id']})
            time.sleep(1)
        liked_posts = []

        print('Лайкнутые посты:')
        for post in posts.items():
            try:
                itemID = post[0]
                ownerID = post[1]
                timeOut = 5
                isLiked = vk_api.likes.isLiked(user_id=user_id, item_id=post[0], type='post', owner_id=post[1], timeout=5)
            except Exception:
                isLiked = 0

            if isLiked:
                print('vk_helper.com/wall{}_{}'.format(post[1], post[0]))
                liked_posts.append('vk.com/wall{0}_{1}'.format(post[1], post[0]))
            time.sleep(0.6)
        return liked_posts