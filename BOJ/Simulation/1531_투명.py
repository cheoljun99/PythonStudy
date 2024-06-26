# -*- coding: utf-8 -*-

N,M=map(int,input().split())
# 101x101 크기의 2차원 리스트 초기화
board=[[0 for x in range(101)] for x in range(101)]#리스트 컴플기헨션

while N>0:
    X1,Y1,X2,Y2=map(int,input().split())
    
    height=Y2-Y1
    row=X2-X1
    
    for Y_point in range(Y1,Y1+height+1):
        for X_point in range(X1,X1+row+1):
            board[Y_point][X_point]+=1
    
    N-=1

ans=0
for i in range(0,101):
    for j in range(0,101):
        if board[i][j]>M:
            ans+=1
            
print(ans)
