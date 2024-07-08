# -*- coding: utf-8 -*-


def main():
    N,M = map(int,input().split())
    arr = [0]*101
    for i in range(0,M):
        i,j,k=map(int,input().split())
        for idx in range(i,j+1):
            arr[idx]=k
      

    for i in range(1,N+1):
        print(arr[i],end=' ')
        
    return



if __name__ == "__main__":
    main()
    