from collections import deque

def solution(n, paths, gates, summits):
    s_paths = sorted(paths, key=lambda x: x[2])
    
    left = min(list(zip(*paths))[2])-1
    right = max(list(zip(*paths))[2])
    mid = (left + right) // 2
    intensity = 10000000
    
    while True:
        if is_hikable(n, s_paths, mid, gates, summits):
            right = mid
        else:
            left = mid
        mid = (left + right) // 2
        
        if right == left + 1:
            intensity = right
            break
    
    # print(intensity)
    summit = get_min_summit(n, s_paths, intensity, gates, summits)
    # summit = 1
    answer = [summit, intensity]
    return answer    

def get_connections(n, paths, intensity):
    connections = {}
    for i in range(n):
        connections[i+1] = []
    
    for i, p in enumerate(paths):
        i, j, w = p
        
        if w > intensity:
            break
            
        connections[i].append(j)
        connections[j].append(i)
    
    return connections

def get_links(n, start, end, connections):
    queue = deque(start)
    visited = [False for _ in range(n+1)]
    while queue:
        current = queue.popleft()
        
        if visited[current]:
            continue            
        
        else:   
            visited[current] = True
            if not end[current]:
                queue+=connections[current]
    
    return visited
    

def is_hikable(n, paths, intensity, gates, summits):
    connections = get_connections(n, paths, intensity)
    end = [True if i in gates else False for i in range(n+1)]
    links_from_summits = get_links(n, summits, end, connections)
    
    for g in gates:
        if links_from_summits[g]:
            return True
    
    return False

def get_min_summit(n, paths, intensity, gates, summits):
    connections = get_connections(n, paths, intensity)
    end = [True if i in summits else False for i in range(n+1)]
    links_from_gates = get_links(n, gates, end, connections)
    
    for s in sorted(summits):
        if links_from_gates[s]:
            return s
    
    return False
