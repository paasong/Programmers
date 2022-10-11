def solution(id_list, report, k):

    person_re = []
    user_num = 0
    report_num = 1

    report_info = dict()
    mail_info = dict()

    for i in id_list:
        report_info[i] = set()
        mail_info[i] = 0

    for user in report:
        user_re = user.split()
        report_info[user_re[report_num]].add(user_re[user_num])


    for i in id_list:
        if k <= len(report_info[i]):
            for j in report_info[i]:
                mail_info[j] += 1

    return list(mail_info.values())


print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"], 3))