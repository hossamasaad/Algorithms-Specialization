# Tarjan algorithm to count Strongly Connected Component
  
adjList = [[1],[2],[0],[4,7],[5],[0,6],[0,2,4],[3,5]]

UNVISITED = -1

onStack = [False] * len(adjList)
IDS = [UNVISITED] * len(adjList)
low_link = [0] * len(adjList)
stack = []
scc = 0
ID = 0

def findSCC():
    for i in range(len(adjList)):
        if IDS[i] == UNVISITED:
            DFS(i)


def DFS(u):
    global ID,scc
    stack.append(u)
    onStack[u] = True
    ID += 1
    low_link[u] = IDS[u] = ID 
    
    for to in adjList[u]:
        if IDS[to] == UNVISITED:
            DFS(to)
        if onStack[to]:
            low_link[u] = min(low_link[u],low_link[to])
            
    if IDS[u] == low_link[u]:
        scc += 1
        print("SCC number :" + str(scc))
        while True:
            v = stack[len(stack) - 1]
            stack.pop()
            onStack[v] = False
            print(v)
            if v == u:
                break

if __name__ == "__main__":
    findSCC()
    
