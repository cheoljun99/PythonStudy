
# -*- coding: utf-8 -*-


def main():
    N,M=map(int,input().split())
    arr=[0]*(N+1)
    
    for i in range(1,N+1):
        arr[i]=i
        
    for i in range(0,M):
        i,k=map(int,input().split())
        temp=arr[i]
        arr[i]=arr[k]
        arr[k]=temp
        
    for i in range(1,N+1):
        print(arr[i],end=' ')
    return



if __name__ == "__main__":
    main()
    