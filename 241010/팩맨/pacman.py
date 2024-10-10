from collections import deque
import copy
m,t=map(int,input().split())

board=[[0]*4 for _ in range(4)]

class monster():
    def __init__(self,y,x,d):
        self.pos=[y,x]
        self.d=d
        self.dead=False

r,c=map(int,input().split())
pack=[r-1,c-1]
info=[]
for _ in range(m):
    y,x,d=map(int,input().split())
    info.append(monster(y-1,x-1,d-1))

def monster_move(info,pack):
    dx=[0,-1,-1,-1,0,1,1,1]
    dy=[-1,-1,0,1,1,1,0,-1]
    for i in range(len(info)):
        fail=False
        if not info[i].dead:
            d=info[i].d
            new_y=info[i].pos[0]+dy[d]
            new_x=info[i].pos[1]+dx[d]
            now=copy.deepcopy(d)
            while new_x<0 or new_x>=4 or new_y<0 or new_y>=4 or [new_y,new_x]==pack or board[new_y][new_x]>=1:
                now=(now+1)%8
                new_y = info[i].pos[0] + dy[now]
                new_x = info[i].pos[1] + dx[now]
                if now==d:
                    fail=True
                    break
            if fail:
                continue

            info[i].pos=[new_y,new_x]
            info[i].d=now
    return info

def pack_move(info,board,pack,t):
    dx=[0,-1,0,1]
    dy=[-1,0,1,0]
    q=deque()
    q.append([0,[],pack[0],pack[1],info])
    #print(q[-1])
    re=[]
    while q:
        eat,path,y,x,infor=q.popleft()
        for i in range(4):
            new_info=copy.deepcopy(infor)
            new_path=copy.deepcopy(path)
            new_eat=copy.deepcopy(eat)
            new_y=y+dy[i]
            new_x=x+dx[i]
            if new_x<0 or new_x>=4 or new_y<0 or new_y>=4:
                continue
            for j in range(len(new_info)):
                if not new_info[j].dead:
                    if new_info[j].pos==[new_y,new_x]:
                        new_eat+=1
                        new_info[j].dead=True
            new_path.append(i)
            if len(new_path)==3:
                re.append([new_eat,new_path,new_y,new_x,new_info])
            else:
                q.append([new_eat,new_path,new_y,new_x,new_info])
    re.sort(key=lambda x:-x[0])
    #print(re)
    info=re[0][4]
    new_info=[]
    for i in range(len(info)):
        if info[i].dead:
            board[info[i].pos[0]][info[i].pos[1]]=t
        elif not info[i].dead:
            new_info.append(info[i])
    pack=[re[0][2],re[0][3]]
    return new_info,board,pack




def siche(board,t):
    for i in range(4):
        for j in range(4):
            if board[i][j]!=0 and (board[i][j]+2)==t:
                board[i][j]=0
    return board

for k in range(1,t+1):
    egg=copy.deepcopy(info)
    monster=monster_move(info,pack)
    info,board,pack=pack_move(info,board,pack,k)
    board=siche(board,k)
    info.extend(egg)

    '''for i in range(4):
        print(*board[i])
    print(pack)'''
print(len(info))
    #print("*"*20)


'''
0 0 0 0
0 2 1 0
0 0 0 0
0 0 1 0

0 1 0 0
0 2 0 0
0 0 0 0
0 0 0 1


'''