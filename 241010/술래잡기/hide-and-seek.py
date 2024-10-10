import copy

n,m,h,k=map(int,input().split())
move_board=[[-1]*n for _ in range(n)]
move_board_2=[[-1]*n for _ in range(n)]
sy,sx=0,0
dx=[0,1,0,-1]
dy=[1,0,-1,0]
#2 1 2 2 3 3 1 1 1
now_d=0
for i in range(n*n):
    new_x=sx+dx[now_d]
    new_y=sy+dy[now_d]
    if  new_x<0 or new_y>=n or new_x>=n or new_y<0 or move_board[new_y][new_x]!=-1:
        now_d=(now_d+1)%4
        new_x = sx + dx[now_d]
        new_y = sy + dy[now_d]
    move_board[sy][sx]=now_d
    move_board_2[new_y][new_x]=(now_d+2)%4
    if new_y==(n//2) and new_x==(n//2):
        break
    sy,sx=new_y,new_x


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

board=[[0]*n for _ in range(n)]
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
        now=move_board
    elif new_y==n//2 and new_x==n//2:
        now=move_board_2
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
now=move_board_2
for i in range(k):
    info=move(info,sulre)
    
    sulre,now=move_sulre(sulre,now)
    
    cnt=catch(board,info,sulre)
    answer+=cnt*(i+1)
   
print(answer)