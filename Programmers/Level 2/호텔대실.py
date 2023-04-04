def time_convert(string) :
    h, m = map(int, string.split(":"))
    return h*60 + m

def solution(book_time):
    s_list = [ (time_convert(s),1) for s,e in book_time]
    e_list = [ (time_convert(e)+10,-1) for s,e in book_time]

    book_list = sorted((e_list+s_list), key=lambda x:x[0])

    print('book_list',book_list)
    answer = 0
    book = 0

    for t, c in book_list:
        book += c
        answer = max(answer, book)



    return answer


print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))