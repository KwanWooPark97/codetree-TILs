from collections import deque
n,m=map(int,input().split())

board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))

d=0
dice=[1,2,3,4,5,6]
def dice_rotate(board,dice,pos,d):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    y,x=pos
    if board[y][x]<dice[5]:
        d=(d+1)%4
    elif board[y][x]>dice[5]:
        d=(d-1)%4
    new_y,new_x=pos[0]+dy[d],pos[1]+dx[d]
    if new_x<0 or new_x>=n or new_y<0 or new_y>=n:
        d=(d+2)%4
    return d

def dice_move(dice,pos,d):
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    pos=[pos[0]+dy[d],pos[1]+dx[d]]
    if d==0:#오른
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif d==1:#아래
        dice=[dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]]
    elif d==2:#왼
        dice=[dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]]
    elif d==3:#위
        dice=[dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]]
    return dice,pos,d
def bfs(board,pos):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    target=board[pos[0]][pos[1]]
    q=deque()
    q.append(pos)
    visited=[[0]*n for _ in range(n)]
    visited[pos[0]][pos[1]]=1
    while q:
        y,x=q.popleft()
        for i in range(4):
            new_y, new_x = y + dy[i], x + dx[i]
            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n:
                continue
            if board[new_y][new_x]==target and visited[new_y][new_x]==0:
                q.append([new_y,new_x])
                visited[new_y][new_x]=1
    cnt=0
    for i in range(n):
        cnt+=sum(visited[i])
    return cnt*target

pos=[0,0]
answer=0
for _ in range(m):
    dice,pos,d=dice_move(dice,pos,d)
    answer+=bfs(board,pos)
    d=dice_rotate(board,dice,pos,d)
print(answer)