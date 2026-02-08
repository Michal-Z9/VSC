##a=int(input())
##L=[]
##for i in range(a):
##    L.append(int(input()))
##
##print(L)

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    
    states = [int(c) for c in input_data[2]]
    
    
    adj = [[False] * n for _ in range(n)]
    
    idx = 3
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        adj[u][v] = adj[v][u] = True
        idx += 2

    res = []

  
    
    for i in range(n):
        if states[i] == 1:
            res.append(i + 1)
           
            neighbors = []
            for j in range(n):
                if adj[i][j]:
                    neighbors.append(j)
            
           
            states[i] = 1 - states[i]
            for v in neighbors:
                states[v] = 1 - states[v]
            
                for idx_u in range(len(neighbors)):
                    u = neighbors[idx_u]
                for idx_v in range(idx_u + 1, len(neighbors)):
                    v = neighbors[idx_v]
                    adj[u][v] = adj[v][u] = not adj[u][v]
            
            
            for v in neighbors:
                adj[i][v] = adj[v][i] = not adj[i][v]

   
    possible = True
    if any(s != 0 for s in states):
        possible = False
    else:
        for i in range(n):
            for j in range(i + 1, n):
                if adj[i][j]:
                    possible = False
                    break
            if not possible: break

    if possible:
        print("TAK")
        print(len(res))
        print(*(res))
    else:
        print("NIE")

if __name__ == "__main__":
    solve()

