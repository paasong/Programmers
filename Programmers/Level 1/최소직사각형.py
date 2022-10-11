def solution(sizes):
    wl = list()
    hl = list()

    for w, h in sizes:
        if w < h :
            w, h = h, w

        wl.append(w)
        hl.append(h)


    return max(wl)*max(hl)
print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))