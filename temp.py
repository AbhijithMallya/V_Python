from queue import PriorityQueue
v=6
graph=[ [] for i in range(v)]

def bfs(src , target,n):
    visited=[False]*n
    pq=PriorityQueue()
    pq.put((0,src))
    visited[src]=True
    while pq.empty() ==False:
        u=pq.get()[1]
        print(u,end=' ')
        for  v,c in graph[u]:
            if visited[v]==False:
                visited[v]=True
                pq.put((c,v))
            
def add_edge(x,y,cost):
    graph[x].append((y,cost))
    graph[y].append((x,cost))

add_edge(0,1,2)
add_edge(0,2,8)
add_edge(0,3,6)
add_edge(1,4,4)
add_edge(1,5,10)
bfs(0,5,6)
    