def solution(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1

    for phone_number in phone_book:
        temp = ''
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                return False
    return True

print(solution(["999999",'78944','459126','78945','1000000','1100000','101111']))


