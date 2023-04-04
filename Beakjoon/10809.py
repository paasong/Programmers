alphabet = [-1 for _ in range(26)]

a = map(str,input())

for i, alp in enumerate(a):
    idx = ord(alp)%97
    if alphabet[idx] == -1:
        alphabet[idx] = i

for alp in alphabet:
    print(alp)