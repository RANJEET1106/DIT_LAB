def dfs(vertex,adj_list,visited):
    visited[vertex]=True
    print(f"Visited: {vertex}")
    for i in adj_list[vertex]:
        if not visited[i]:
            dfs(i,adj_list,visited)

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
dfs(start,adj_ist,visited)