from collections import deque
n,m,k=map(int,input().split())

board=[]

for _ in range(n):
    board.append(list(map(int,input().split())))

class team_info():
    def __init__(self,y,x):
        self.head=[y,x]
        self.tail=[[y,x]]
team=[]
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            team.append(team_info(i,j))

def find_tail(team):

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited=[[0]*n for _ in range(n)]
    for i in range(len(team)):
        q = deque()
        q.append(team[i].head)
        visited[team[i].head[0]][team[i].head[1]]=1
        while q:
            y,x=q.popleft()
            for j in range(4):
                new_y = y + dy[j]
                new_x = x + dx[j]
                if 0 <= new_y < n and 0 <= new_x < n and (board[new_y][new_x] == 2 or board[new_y][new_x]==3) and visited[new_y][new_x]==0:
                    visited[new_y][new_x]=1
                    if board[new_y][new_x]==2:
                        team[i].tail.append([new_y,new_x])
                        q.append([new_y,new_x])
                    elif board[new_y][new_x]==3:
                        team[i].tail.append([new_y, new_x])

    return team



def move(board,team):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    for i in range(len(team)):
        sy,sx=team[i].head
        for j in range(4):
            new_y=sy+dy[j]
            new_x=sx+dx[j]
            if 0<=new_y<n and 0<=new_x<n and board[new_y][new_x]==4:
                break
        team[i].head=[new_y,new_x]
        new_tail=[[new_y,new_x]]
        board[new_y][new_x]=1
        for j in range(len(team[i].tail)-1):
            board[team[i].tail[j][0]][team[i].tail[j][1]]=2
            new_tail.append(team[i].tail[j])
        else:
            board[team[i].tail[j][0]][team[i].tail[j][1]] = 3
            board[team[i].tail[-1][0]][team[i].tail[-1][1]]=4
        team[i].tail=new_tail

    return board,team

def throw(round,r,board):
    if round==0:
        for i in range(n):
            if board[r][i]!=4 and board[r][i]!=0:
                return r,i
    elif round==1:
        for j in range(n)[::-1]:
            if board[j][r]!=4 and board[j][r]!=0:
                return j,r
    elif round==2:

        for j in range(n)[::-1]:
            if board[r][j]!=4 and board[r][j]!=0:
                return r,j
    elif round==3:
        for i in range(n):
            if board[i][r]!=4 and board[i][r]!=0:
                return i,r
    return -1,-1
team=find_tail(team)
answer=0
for i in range(k):
    board,team=move(board,team)
    if i<n:
        round=0
    elif i<2*n:
        round=1
    elif i<3*n:
        round=2
    elif i<4*n:
        round=3
    y,x=throw(round,i-((n)*round),board)
    #print(y,x)
    if y==-1 and x==-1:
        continue
    for j in range(len(team)):
        if [y,x] in team[j].tail:
            answer+=(team[j].tail.index([y,x])+1)**2
            team[j].tail=team[j].tail[::-1]
            team[j].head=team[j].tail[0]
            for v in range(len(team[j].tail) - 1):
                board[team[j].tail[v][0]][team[j].tail[v][1]] = 2
            else:
                board[team[j].head[0]][team[j].head[1]]=1
                board[team[j].tail[-1][0]][team[j].tail[-1][1]] = 3
            break
    '''for i in range(n):
        print(*board[i])
    print(answer)
    print("*"*20)'''
print(answer)