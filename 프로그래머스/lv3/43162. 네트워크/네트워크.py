def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for i in range(n) :
        if visited[i] == False :
            BFS(n, computers, i, visited)
            answer += 1
    return answer

def BFS(n, computers, i, visited) :
    visited[i] = True
    queue = []
    queue.append(i)
    while len(queue) != 0 :
        i = queue.pop(0)
        visited[i] = True
        for connect in range(n) :
            if connect != i and computers[i][connect] == 1 :
                if visited[connect] == False :
                    queue.append(connect)