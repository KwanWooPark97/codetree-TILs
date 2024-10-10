import copy
from collections import deque
n,m,h,k=map(int,input().split())

path=[[0,0]]
d=[0]
d_2=[2]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
for i in range(n*n):
    now_d=d[-1]
    new_x=path[-1][1]+dx[now_d]
    new_y=path[-1][0]+dy[now_d]
    if [new_y,new_x] in path or new_x<0 or new_y>=n or new_x>=n or new_y<0:
        now_d=(now_d+1)%4
        new_x = path[-1][1] + dx[now_d]
        new_y = path[-1][0] + dy[now_d]
    path.append([new_y,new_x])
    d.append(now_d)
    d_2.append((now_d+2)%4)
    if new_y==(n//2) and new_x==(n//2):
        break
d_2.reverse()
board=[[0]*n for _ in range(n)]
path=deque(path)
d=deque(d)
d_2=deque(d_2)
path_2=copy.deepcopy(path)
path_2.reverse()
class doduk():
    def __init__(self,y,x,dd):
        self.pos=[y,x]
        self.arrow=dd
        self.dead=False
info=[]
for i in range(m):
    y,x,dd=map(int,input().split())
    info.append(doduk(y-1,x-1,dd))

for i in range(h):
    y,x=map(int,input().split())
    board[y-1][x-1]=1

def move(now,info):
    dx=[0,1,0,-1,0]
    dy=[0,0,1,0,-1]
    for i in range(len(info)):
        dist=abs(now[0][0]-info[i].pos[0]) + abs(now[0][1]-info[i].pos[1])
        if not info[i].dead and dist<=3:
            new_y=info[i].pos[0]+dy[info[i].arrow]
            new_x=info[i].pos[1]+dx[info[i].arrow]
            if new_y==n:
                info[i].arrow+=2
                new_y=info[i].pos[0]+dy[info[i].arrow]
            elif new_y==-1:
                info[i].arrow -= 2
                new_y = info[i].pos[0] + dy[info[i].arrow]
            if new_x == n:
                info[i].arrow += 2
                new_x = info[i].pos[1] + dx[info[i].arrow]
            elif new_x == -1:
                info[i].arrow -= 2
                new_x = info[i].pos[1] + dx[info[i].arrow]
            if now[0]!=[new_y,new_x]:
                info[i].pos=[new_y,new_x]
    return info

def move_sulre(now,dd):
    y,x=now.popleft()
    dd.popleft()

    if len(now)==0:
        if y==0 and x==0:
            now=copy.deepcopy(path)
            dd=copy.deepcopy(d)
        elif y==n//2 and x==n//2:
            now = copy.deepcopy(path_2)
            dd = copy.deepcopy(d_2)
    return now,dd
def catch(board,now,dd,info):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    y,x=now[0]
    arrow=dd[0]
    cnt=0
    for i in range(3):
        new_y=y+(dy[arrow]*i)
        new_x=x+(dx[arrow]*i)
        for j in range(len(info)):
            if not info[j].dead and info[j].pos==[new_y,new_x] and board[new_y][new_x]!=1:
                cnt+=1
                info[j].dead=True
    return cnt

now=copy.deepcopy(path_2)
dd=copy.deepcopy(d_2)
answer=0
for i in range(k):
    info=move(now,info)
    now,dd=move_sulre(now,dd)
    #print(now[0],dd[0])
    cnt=catch(board, now, dd, info)
    answer+=cnt*(i+1)
print(answer)