# Topoligical Sort
  
adjList = [[1],[2,3,4],[5],[5],[5],[],[7],[]]

#            2
#          /   \
#   0 >> 1 > 3 > 5    6 > 7
#          \   /
#            4

visited = [False] * len(adjList)


def DFS(u):
    visited[u] = True
    path = []
    for e in adjList[u]:
        if visited[e] == False:
            path += DFS(e)
    path.append(u)
    return path
    
if __name__ == "__main__":
    path = []
    for x in range(len(adjList)):
        print("X is :" + str(x))
        if visited[x] == False:
            path += DFS(x)
    print(path)
