from collections import deque

def bfs(q,adj_list,visited):
    if not q:
        return
    
    current=q.popleft()
    print(f"Visited: {current}")

    for i in adj_list[current]:
        if not visited[i]:
            visited[i]=True
            q.append(i)
    bfs(q,adj_list,visited)

n=int(input("Enter the numer of vertices: "))
e=int(input("Enter the number of vertices: "))

visited=[False]*n
adj_ist=[[] for i in range(n)]

for i in range(e):
    print("Enter the edge in form of u v : ")
    u,v=map(int,input().split())

    adj_ist[u].append(v)
    adj_ist[v].append(u)

start=int(input("Enter the starting vertex: "))
visited[start]=True

q=deque()
q.append(start)

bfs(q,adj_ist,visited)
