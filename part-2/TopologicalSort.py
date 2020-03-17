# Topological Sort
  
adjList = [[1],[2,3,4],[5],[5],[5],[]]

#            2
#          /   \
#   0 >> 1 > 3 > 5 
#          \   /
#            4

visited = [False] * len(adjList)


def DFS(u):
    visited[u] = True
    path = []
    for x in adjList[u]:
        if visited[x] == False:
            path += DFS(x)
    path.append(u)
    return path
    
if __name__ == "__main__":
    path = DFS(0)
    print(path)
