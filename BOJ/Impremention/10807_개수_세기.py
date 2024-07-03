# -*- coding: utf-8 -*-


def main():
    N=int(input().strip())
    
    vec=list(map(int,input().split()))
    
    v=int(input().strip())
    
    ans=0
    for i in vec:
        if v==i:
            ans=1+ans
          
    print(ans)
    return



if __name__ == "__main__":
    main()
    