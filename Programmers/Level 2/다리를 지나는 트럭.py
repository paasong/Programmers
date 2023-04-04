def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0]*bridge_length
    truck_sum = 0
    while bridge:
        truck_sum -= bridge[0]
        truck_sum += bridge[-1]
        bridge.pop(0)
        answer += 1

        if truck_weights:
            if truck_sum+truck_weights[0] <= weight :
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return answer


print(solution(	100, 100, [10]))