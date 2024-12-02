# 그래프(Graph)와 탐색 알고리즘

## 1. 그래프(Graph)란 무엇인가요?

그래프는 **노드(Node, 정점)**와 **간선(Edge, 연결선)**으로 이루어진 자료 구조입니다.  
현실 세계에서의 지하철 노선도, 도로 지도, 친구 관계 등이 그래프의 예입니다.

- **노드(Node)**: 데이터나 상태를 나타내는 점.
- **간선(Edge)**: 노드 간의 연결을 나타내는 선.

그래프는 복잡한 관계를 표현할 수 있어 알고리즘에서 많이 사용됩니다.

---

## 2. 탐색(Traversal)이란 무엇인가요?

탐색은 그래프에서 필요한 정보를 찾기 위해 노드들을 방문하는 과정을 말합니다.  
모든 노드를 방문하거나 특정 조건에 맞는 노드를 찾을 때 사용합니다.

### 대표적인 탐색 방법:
1. **DFS(깊이 우선 탐색)**: 최대한 깊이 내려가면서 탐색.
2. **BFS(너비 우선 탐색)**: 현재 노드와 가까운 노드부터 탐색.

---

## 3. 자료 구조 소개

DFS와 BFS를 구현하기 위해 몇 가지 기본적인 자료 구조를 이해해야 합니다.

### 1) 스택(Stack)
- **개념**: 데이터를 쌓아 올린 형태의 자료 구조.
- **특징**: 마지막에 넣은 데이터가 가장 먼저 나온다. 이를 **LIFO(Last In, First Out)**이라고 합니다.

#### 연산
- `push`: 데이터를 스택에 넣기.
- `pop`: 스택에서 데이터를 꺼내기.

#### 예시
```python
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack.pop())  # 출력: 3
print(stack.pop())  # 출력: 2
```

---

### 2) 큐(Queue)
- **개념**: 줄을 서는 형태의 자료 구조.
- **특징**: 먼저 넣은 데이터가 먼저 나온다. 이를 **FIFO(First In, First Out)**이라고 합니다.

#### 연산
- `enqueue`: 데이터를 큐에 넣기.
- `dequeue`: 큐에서 데이터를 꺼내기.

#### 예시
```python
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue.popleft())  # 출력: 1
print(queue.popleft())  # 출력: 2
```

---

### 3) 데크(Deque)
- **개념**: 양쪽 끝에서 데이터를 넣고 뺄 수 있는 자료 구조.
- **특징**: 스택과 큐의 기능을 모두 가짐.

#### 연산
- `append`: 오른쪽 끝에 데이터 추가.
- `appendleft`: 왼쪽 끝에 데이터 추가.
- `pop`: 오른쪽 끝에서 데이터 꺼내기.
- `popleft`: 왼쪽 끝에서 데이터 꺼내기.

#### 예시
```python
from collections import deque

deque_obj = deque()
deque_obj.append(1)
deque_obj.appendleft(2)
deque_obj.append(3)
print(deque_obj.popleft())  # 출력: 2
print(deque_obj.pop())      # 출력: 3
```

---

## 4. DFS(깊이 우선 탐색)

### 개념과 원리
- **개념**: 한 노드에서 시작하여 갈 수 있는 깊은 곳까지 탐색한 후, 다시 돌아와 다른 경로를 탐색하는 방법.

#### 원리
1. 시작 노드를 방문하고 **스택**에 넣습니다.
2. 스택의 최상단 노드에 연결된 방문하지 않은 노드가 있으면 그 노드를 방문하고 스택에 넣습니다.
3. 방문하지 않은 노드가 없으면 스택에서 노드를 꺼냅니다.
4. 스택이 빌 때까지 반복합니다.

---

### 스택을 이용한 DFS 구현
```python
def dfs_stack(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()  # 스택에서 최상단 노드 꺼내기
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')
            # 현재 노드에 연결된 노드를 스택에 추가
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)
```

---

### 재귀 함수를 이용한 DFS 구현
```python
def dfs_recursive(graph, vertex, visited=set()):
    visited.add(vertex)
    print(vertex, end=' ')
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
```

---

## 5. BFS(너비 우선 탐색)

### 개념과 원리
- **개념**: 시작 노드에서 가까운 노드부터 순서대로 탐색하는 방법.

#### 원리
1. 시작 노드를 방문하고 **큐**에 넣습니다.
2. 큐에서 노드를 꺼내 해당 노드에 연결된 방문하지 않은 노드를 모두 큐에 넣습니다.
3. 방문한 노드를 표시합니다.
4. 큐가 빌 때까지 반복합니다.

---

### 큐를 이용한 BFS 구현
```python
from collections import deque

def bfs_queue(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        vertex = queue.popleft()  # 큐에서 노드 꺼내기
        print(vertex, end=' ')
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

---

## 6. 예제 문제 풀이

### 그래프 예시
```python
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6, 7],
    4: [2],
    5: [2],
    6: [3],
    7: [3]
}
```

#### DFS 실행
```python
dfs_recursive(graph, 1)
# 출력: 1 2 4 5 3 6 7
```

#### BFS 실행
```python
bfs_queue(graph, 1)
# 출력: 1 2 3 4 5 6 7
```

---

## 7. 정리

- **그래프(Graph)**: 노드와 간선으로 이루어진 자료 구조.
- **탐색(Traversal)**: 그래프의 노드를 방문하는 방법.
- **스택(Stack)**: LIFO 구조로 DFS 구현에 사용.
- **큐(Queue)**: FIFO 구조로 BFS 구현에 사용.
- **데크(Deque)**: 양쪽 끝에서 데이터의 삽입과 삭제가 가능한 자료 구조.
- **DFS(깊이 우선 탐색)**: 최대한 깊이 내려가며 탐색하는 방법.
- **BFS(너비 우선 탐색)**: 현재 노드와 가까운 노드부터 탐색하는 방법.

**추가 팁**
- 그래프 표현 방법: 딕셔너리나 리스트를 이용하여 인접 리스트 형태로 표현할 수 있습니다.
- 방문 기록(Visited): 이미 방문한 노드를 기록하여 무한 루프를 방지합니다.
- 연습 방법: 작은 그래프부터 시작하여 손으로 방문 순서를 적어보면서 연습하세요.

