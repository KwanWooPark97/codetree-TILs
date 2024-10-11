from collections import deque
r,c,k=map(int,input().split())
r+=3
board=[[0]*c for _ in range(r)]
move=[]
for x in range(k):
    move.append(list(map(int,input().split())))
def drop(board,x,d,now):
    cnt=0
    while True:
        if (cnt+2)<r and (now+1)<c and 0<=(now-1) and board[cnt+2][now]==0 and board[cnt+1][now-1]==0 and board[cnt+1][now+1]==0:
            cnt+=1
        elif (cnt+2)<r and 0<=(now-2) and board[cnt][now-2]==0 and board[cnt-1][now-1]==0 and board[cnt+1][now-1]==0 and board[cnt+2][now-1]==0 and board[cnt+1][now-2]==0:
            cnt+=1
            now-=1
            d=(d-1)%4
        elif (cnt+2)<r and (now+2)<c and board[cnt][now+2]==0 and board[cnt-1][now+1]==0 and board[cnt+1][now+1]==0 and board[cnt+2][now+1]==0 and board[cnt+1][now+2]==0:
            cnt+=1
            now+=1
            d=(d+1)%4
        else:
            break
    board[cnt][now]=x
    board[cnt][now+1]=x
    board[cnt][now-1]=x
    board[cnt+1][now]=x
    board[cnt-1][now]=x
    if d==0:
        ex.append([cnt-1,now])
    elif d==1:
        ex.append([cnt,now+1])
    elif d==2:
        ex.append([cnt+1,now])
    elif d==3:
        ex.append([cnt,now-1])
    return board,cnt,now,ex

def bfs(board,y,x,ex):
    dx=[0,-1,1,0]
    dy=[-1,0,0,1]
    q=deque()
    q.append([y,x])
    visited=[[0]*c for _ in range(r)]
    visited[y][x]=1
    while q:
        ny,nx=q.popleft()
        for i in range(4):
            new_y,new_x=ny+dy[i],nx+dx[i]
            if new_y<0 or new_y>=r or new_x<0 or new_x>=c:
                continue
            if visited[new_y][new_x]==0 and (board[ny][nx]==board[new_y][new_x] or (board[new_y][new_x]!=0 and ex[board[ny][nx]-1]==[ny,nx])):
                visited[new_y][new_x]=1
                q.append([new_y,new_x])
    cnt=0
    '''for i in range(r):
        print(*visited[i])'''
    for i in range(r)[::-1]:
        if sum(visited[i])!=0:
            cnt=i-2
            break
    return cnt
answer=0
ex=[]
for x in range(k):
    now,d=move[x]
    board,y,now,ex=drop(board,x+1,d,now-1)
    if y<=3:
        board=[[0]*c for _ in range(r)]
        continue
    answer+=bfs(board,y,now,ex)
    '''for i in range(r):
        print(*board[i])'''
    #print(ex)
print(answer)
    #print("*"*20)