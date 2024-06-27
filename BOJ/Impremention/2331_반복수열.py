# -*- coding: utf-8 -*-

A,P=map(int,input().split())

un_map={} # unordered_map와 같은 역할을 하는 Python dict

un_map[A] = 0

while un_map[A]<2:
    un_map[A]+=1
    num=0
    while (A/10) !=0:
        num+=(A%10)**P #제곱은 **연산자 사용
        A //=10 #정수 나누기
    if A != 0:
        num += A ** P
        
    A=num
    if A in un_map:
        continue
    else:
        un_map[A]=0

ans=0
for key, value in un_map.items():
    if value == 1:
        ans+=1

print(ans)

