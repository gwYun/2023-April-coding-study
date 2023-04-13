from pprint import pprint
import sys
from itertools import permutations
from copy import deepcopy
input = sys.stdin.readline

min_count = int(1e9)
#board = [list(map(int,input().split())) for _ in range(10)]

total = 0
board = []
for i in range(10):
    line = list(map(int,input().split()))
    board.append(line)
    for j in range(10):
        if line[j]==1:
            total+=1
        

def check(x,y,k):
    for i in range(x,x+k):
        for j in range(y,y+k):
            if not (0<=i<10 and 0<=j<10 and board[i][j]==1):
                return False
    return True

def cover(x,y,k):
    global board
    for i in range(x,x+k):
        for j in range(y,y+k):
            board[i][j]=k+10

def recover(x,y,k):
    global board
    for i in range(x,x+k):
        for j in range(y,y+k):
            board[i][j]=1
            
def update_count(count):
    global min_count
    min_count = min(min_count,count)


def dfs(count,_board,kill):
    global total,board
    print(count,kill,total, min_count)
    pprint(board)
    if total ==kill:
        update_count(count)
        return
    
    board = deepcopy(_board)
    update = False
    for x in range(10):
        for y in range(10):
            if board[x][y]==1:
                for k in range(5,0,-1):
                    if check(x,y,k):
                        cover(x,y,k)
                        update = True
                        dfs(count+1,board,kill+k*k)
                    else:
                        break
    

dfs(0,board,0)
print(min_count)

'''
0 0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0



1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 1 1 0 1 1
1 1 0 1 1 1 1 0 1 1
1 1 0 1 1 0 0 1 1 1
1 1 1 0 0 0 0 1 1 1
1 1 1 1 1 1 0 1 1 1
1 1 1 1 1 1 0 0 1 1
0 0 0 1 1 1 0 0 1 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
13

0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 1 0 0
0 0 1 1 1 1 1 1 0 0
0 0 1 1 1 1 1 1 0 0
0 0 1 1 1 1 1 1 0 0
0 0 1 1 1 1 1 1 0 0
0 0 1 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
4


1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 1 1 0 1 1
1 1 0 1 1 1 1 0 1 1
1 1 0 1 1 0 0 1 1 1
1 1 1 0 0 0 0 1 1 1
1 1 1 1 1 1 0 1 1 1
1 1 1 1 1 1 0 0 1 1
0 0 0 1 1 1 0 0 1 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
13


1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 0 0 0 0 0
1 1 1 1 1 0 0 0 0 0
1 1 1 1 1 0 0 0 0 0
1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0


4 4 4 4 3 3 3 0 0 0
4 4 4 4 3 3 3 0 0 0
4 4 4 4 3 3 3 0 0 0
4 4 4 4 1 2 2 0 0 0
5 5 5 5 5 2 2 0 0 0
5 5 5 5 5 0 0 0 0 0
5 5 5 5 5 0 0 0 0 0
5 5 5 5 5 0 0 0 0 0
5 5 5 5 5 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

답 : 5

'''