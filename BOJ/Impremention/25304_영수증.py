# -*- coding: utf-8 -*-


def main():
    X=int(input().strip())
    N=int(input().strip())
    
    for i in range(0,N):
        price, num=map(int,input().split())
        X=X-price*num
    
    if X!=0:
        print("No")
        
    else:
        print("Yes")
        
    
    return



if __name__ == "__main__":
    main()
    