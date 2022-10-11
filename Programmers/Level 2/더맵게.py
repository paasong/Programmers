def solution(scoville, K):
    scoville = scoville
    scoville.sort()
    scoville.insert(0, None)

    cnt = 0
    try:
        while scoville[1] < K :
            if len(scoville) == 2:
                return -1
            first = pop(scoville)
            second = pop(scoville)
            sco_insert(scoville, first + second * 2)
            cnt += 1
    except:
        return -1

    return cnt


def pop(scoville):

    popped_val = scoville[1]
    inserted_val = scoville[-1]
    del scoville[-1]
    sco_down(scoville, inserted_val)
    return popped_val

def sco_down(scoville, insert_val):
    idx = 1
    compare_idx = 0
    while idx < len(scoville):
        if compare_idx == idx :
            break
        compare_idx = idx
        # pop에서 [1] 자리를 None으로 비워놓을 것임
        scoville[idx] = insert_val
        #idx
        left_idx = idx * 2
        right_idx = idx * 2 + 1

        # Not exist child node
        if left_idx >= len(scoville):
            pass
        # Not right child node
        elif right_idx >= len(scoville):
            if scoville[idx] > scoville[left_idx]:
                scoville[idx], scoville[left_idx] = scoville[left_idx], scoville[idx]
                idx += left_idx
            else:
                pass
        # exist both node
        else:
            if scoville[left_idx] <= scoville[right_idx] and scoville[idx] > scoville[left_idx]:
                scoville[idx], scoville[left_idx] = scoville[left_idx], scoville[idx]
                idx = left_idx
            elif scoville[left_idx] > scoville[right_idx] and scoville[idx] > scoville[right_idx]:
                scoville[idx], scoville[right_idx] = scoville[right_idx], scoville[idx]
                idx = right_idx

    return scoville

def sco_insert(scoville,inserted_val):

    scoville.append(inserted_val)
    inserted_idx = len(scoville)-1

    while True:
        if sco_up(scoville,inserted_idx) == False:
            break
        else:
            parent_idx = inserted_idx // 2
            scoville[inserted_idx], scoville[parent_idx] = scoville[parent_idx], scoville[inserted_idx]
            inserted_idx = parent_idx
    return scoville

def sco_up(scoville, inserted_idx):
    if inserted_idx <= 1:
        return False
    parent_idx = inserted_idx // 2
    if scoville[inserted_idx] < scoville[parent_idx]:
        return True
    else:
        return False

import heapq

def solution1(scoville, K):
    heapq.heapify(scoville)
    count = 0

    while scoville:
        first = heapq.heappop(scoville)
        if first >= K:
            return count
        if not scoville:
            break
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)
        count += 1

    return -1

id = 50
print(solution1([1, 2, 3, 9, 10, 12], id))
print(solution([1,1,1,1,1,1,100,100,100,100,0,0,0,0,0], id))