# BFS
# 너비 우선 탐색 (가까운 노드부터 우선 탐색)
# 큐 자료구조 이용
# 1. 탐색 시작 노드를 큐에 삽입 후 방문 처리
# 2. 큐에서 노드를 꺼낸 뒤 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입 후 방문 처리
# 3. 2번 과정을 수행할 수 없을 때까지 반복

from collections import deque

def bfs(graph, start, visited):
    
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
# 각 노드가 연결된 그래프
graph = [
    [], # 1번부터 하기위해
    [2,3,8], # 인덱스가 노드번호, 리스트는 인접 노드 인덱스 번호
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보 (인덱스가 노드 번호)
visited = [False] * 9

bfs(graph, 1, visited)