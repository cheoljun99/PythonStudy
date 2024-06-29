# -*- coding: utf-8 -*-


def main():
    N=int(input())

    vec =[]
    
    for i in range(0,N):
        points = list(map(int, input().split()))
        vec.append((points[0],points[1]))
        
    vec = sorted(vec, key=lambda x: (x[0], x[1])) # stable_sort 대신 sorted 사용
    
    for X, Y in vec:
        print(X,Y)
        
    return



if __name__ == "__main__":
    main()