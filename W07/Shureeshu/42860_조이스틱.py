# 42860_조이스틱
# return : 조이스틱 조작 횟수의 최솟값
def solution(name):
    answer = len(name) - 1
    
    # 순회의 수 구하기
    graph = [0]
    for char in name:
        if char == 'A':
            graph [-1] += 1
        else:
            answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
            graph.append(1)
    
    route_1 = graph[-1]
    route_2 = graph[0] - 1
    length_A = max(graph) - 1
    i = name.find('A'*length_A)
    j = len(name) - i - length_A
    if i != 0 and j != 0:
        route_3 = length_A - min(i-1, j)
    
    answer -= max(route_1, route_2, route_3)

    return answer

from collections import deque
name = "BBBAAAABA"


print(solution(name))
# name = "JEROEN"
# print(solution(name))
# name = "JAN"
# print(solution(name))
# 1: 커서 순방향 순회 vs 역방향 순회
# 2: 각 위치에서 순방향 순회 vs 역방향 순회