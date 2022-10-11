def solution(record):
    result = list()
    user_info = dict()

    state = 0
    id= 1
    nickname = 2



    for log in record:
        split_log=log.split()

        try:
            user_info[split_log[id]] = split_log[nickname] # 닉네임 계속 갱신
        except:
            pass

    for log in record:
        split_log = log.split()
        if split_log[state] == 'Enter':
            result.append("{}님이 들어왔습니다.".format(user_info[split_log[id]]))

        elif split_log[state] == 'Leave':
            result.append("{}님이 나갔습니다.".format(user_info[split_log[id]]))
        else:
            pass


    return result


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
