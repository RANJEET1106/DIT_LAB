import sys

def min_key(key,in_mst,n):
    min_val=sys.maxsize
    min_index= -1
    for i in range(n):
        if not in_mst[i] and key[i]<min_val:
            min_val=key[i]
            min_index=i
    return min_index

def prims_mst(graph,n):
    key=[sys.maxsize]*n
    parent=[None] *n
    in_mst=[False]*n

    key[0]=0
    parent[0]=-1

    for i in range(n-1):
        u=min_key(key,in_mst,n)
        in_mst[u]=True

        for v in range(n):
            if graph[u][v]!=0 and not in_mst[v] and graph[u][v]<key[v]:
                parent[v]=u
                key[v]=graph[u][v]
    
    print("Edge \t Weight")
    for i in range(1,n):
        print(f"{parent[i]} - {i} \t {graph[i][parent[i]]}")


n=int(input("Enter the number of vertices: "))
graph=[]

print("Enter the adjacency matrix (space-separated, use 0 for no edge): ")
for i in range(n):
    row=list(map(int,input().split()))
    graph.append(row)

print("\nMin Spanning tree using prims algorithm: ")
prims_mst(graph,n)
