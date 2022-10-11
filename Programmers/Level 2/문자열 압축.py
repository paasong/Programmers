# def solution(s):
#     answer = len(s)
#     for step in range(1,(len(s)//2) + 1):  # 단계
#         print('step : ', step)
#         ans = ''
#         tmp_ans = s[:step]
#
#         cnt = 1
#
#         for i in range(0,len(s),step):
#             pred = s[i:i+step]
#             next = s[i+step:i+(2*step)]
#
#             if pred == next:
#                 cnt += 1
#                 tmp_ans = str(cnt) + next
#             else:
#                 cnt = 1
#                 ans += tmp_ans
#                 tmp_ans = next
#
#         if answer > len(ans):
#             answer = len(ans)
#
#
#     return answer

def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

 print(solution("aabbaccc"))

