# Count number of connected component
  

dx = [1,1,1,-1,-1,-1,0,0]
dy = [0,1,-1,0,1,-1,1,-1]

adjList = [[],[2,5],[1,4,3],[2,4],[3,2],[1],[7,8],[6,8],[6,7]]
visited = [False] * len(adjList)


def DFS(u):
    visited[u] = True
    
    for x in adjList[u]:
        if visited[x] == False:
            DFS(x)

    
if __name__ == "__main__":
    counter = 0
    for i in range(len(adjList)):
        if visited[i] == False:
            counter += 1
            DFS(i)
    print(counter)
