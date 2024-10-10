import copy
from collections import deque
n,m,h,k=map(int,input().split())

board=[[0]*n for _ in range(n)]
path=[[0,0]]
d=[0]
d_2=[2]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
#2 1 2 2 3 3 1 1 1
for i in range(n*n):
    now_d=d[-1]
    new_x=path[-1][1]+dx[now_d]
    new_y=path[-1][0]+dy[now_d]
    if [new_y,new_x] in path or new_x<0 or new_y>=n or new_x>=n or new_y<0:
        now_d=(now_d+1)%4
        new_x = path[-1][1] + dx[now_d]
        new_y = path[-1][0] + dy[now_d]
    path.append([new_y, new_x])
    if new_y==(n//2) and new_x==(n//2):
        break
    nx=new_x+dx[now_d]
    ny=new_y+dy[now_d]

    if [ny,nx] in path or nx<0 or ny>=n or nx>=n or ny<0:
        now_d=(now_d+1)%4

    d.append(now_d)
    d_2.append((now_d+2)%4)
move_board=[[0]*n for _ in range(n)]
move_board_2=[[0]*n for _ in range(n)]


d.append(2)
d_2.reverse()
d_2.append(0)
board=[[0]*n for _ in range(n)]
path=deque(path)
d=deque(d)
d_2=deque(d_2)
path_2=copy.deepcopy(path)
path_2.reverse()
for i in range(len(path)):
    y,x=path[i]
    move_board[y][x]=d[i]
    y,x=path_2[i]
    move_board_2[y][x]=d_2[i]




class doduk():
    def __init__(self,y,x,dd):
        self.pos=[y,x]
        self.arrow=dd
        self.dead=False
sulre=doduk(n//2,n//2,2)

info=[]
for i in range(m):
    y,x,dd=map(int,input().split())
    info.append(doduk(y-1,x-1,dd))

for i in range(h):
    y,x=map(int,input().split())
    board[y-1][x-1]=1

def move(info,sulre):
    dx=[0,1,0,-1,0]
    dy=[0,0,1,0,-1]
    for i in range(len(info)):
        dist=abs(sulre.pos[0]-info[i].pos[0]) + abs(sulre.pos[1]-info[i].pos[1])
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
            if sulre.pos!=[new_y,new_x]:
                info[i].pos=[new_y,new_x]
    return info

def move_sulre(sulre,now):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    new_y=sulre.pos[0]+dy[sulre.arrow]
    new_x=sulre.pos[1]+dx[sulre.arrow]
    if new_y==0 and new_x==0:
        now=copy.deepcopy(move_board)
    elif new_y==n//2 and new_x==n//2:
        now=copy.deepcopy(move_board_2)
    sulre.pos=[new_y,new_x]
    sulre.arrow=now[new_y][new_x]

    return sulre,now

def catch(board,info,sulre):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    y,x=sulre.pos
    arrow=sulre.arrow
    cnt=0
    for i in range(3):
        new_y=y+(dy[arrow]*i)
        new_x=x+(dx[arrow]*i)
        for j in range(len(info)):
            if not info[j].dead and info[j].pos==[new_y,new_x] and board[new_y][new_x]!=1:
                cnt+=1
                info[j].dead=True
    return cnt

answer=0
now=copy.deepcopy(move_board_2)
for i in range(k):
    info=move(info,sulre)
    #print(info[0].pos)
    sulre,now=move_sulre(sulre,now)
    #print(now[0],dd[0])
    cnt=catch(board,info,sulre)
    answer+=cnt*(i+1)
    '''ret=copy.deepcopy(board)
    for j in range(len(info)):
        ret[info[j].pos[0]][info[j].pos[1]]=2
    ret[now[0][0]][now[0][1]]=3
    for j in range(n):

        print(*move_board_2[j])
    print(sulre.pos)
    print("*"*20)'''
print(answer)
'''
5 1 1 39
2 1 1
3 2

0 0 0 0 0
2 0 0 0 0
0 1 3 0 0
0 0 0 0 0
0 0 0 0 0

0 0 0 0 0
0 2 3 0 0
0 1 0 0 0
0 0 0 0 0
0 0 0 0 0

0 0 0 0 0
0 0 2 3 0
0 1 0 0 0
0 0 0 0 0
0 0 0 0 0
1 좌우 우 시작
2 상하 하 시작


'''