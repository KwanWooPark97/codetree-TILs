n,m=map(int,input().split())

board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))

move=[]
for _ in range(m):
    move.append(list(map(int,input().split())))

tree=[[n-1,0],[n-2,0],[n-1,1],[n-2,1]]

def tree_move(board,tree,d,p):
    dy=[0,0,-1,-1,-1,0,1,1,1]
    dx=[0,1,1,0,-1,-1,-1,0,1]

    for i in range(len(tree)):
        y,x=tree[i]
        new_y=(y+dy[d]*p)%n
        new_x=(x+dx[d]*p)%n
        tree[i]=[new_y,new_x]
        board[new_y][new_x]+=1

    return tree,board
def tree_grow(board,tree):
    dx=[-1,1,-1,1]
    dy=[-1,-1,1,1]
    for i in range(len(tree)):
        y,x=tree[i]
        cnt=0
        for j in range(4):
            new_y,new_x=y+dy[j],x+dx[j]
            if 0<=new_x<n and 0<=new_y<n and board[new_y][new_x]>=1:
                cnt+=1
        board[y][x]+=cnt
    return board

for i in range(m):
    d,p=move[i]
    tree,board=tree_move(board,tree,d,p)
    board=tree_grow(board,tree)
    new_tree=[]
    for k in range(n):
        for j in range(n):
            if board[k][j]>=2 and [k,j] not in tree:
                board[k][j]-=2
                new_tree.append([k,j])
    tree=new_tree
answer=0
for i in range(n):
    answer+=sum(board[i])
print(answer)