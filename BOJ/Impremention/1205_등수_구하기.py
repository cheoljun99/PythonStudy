# -*- coding: utf-8 -*-

def cmp(a):
    return -a[0]  # 내림차순 정렬

def main():
    N,new_score,P = map(int, input().split())
    
    vec = []
    if N!=0:
        scores = map(int, input().split())
        for score in scores:
            vec.append((score, 0))
    
    vec.append((new_score, 1))
    
    vec = sorted(vec, key=cmp)  # stable_sort 대신 sorted 사용

    ans = 0
    real_rank = 0
    front_score = 0
    same_rank = 0
    
    for i, (score, check_point) in enumerate(vec):
        if i == 0:
            front_score = score
            real_rank += 1
        else:
            if front_score != score:
                front_score = score
                real_rank += (same_rank + 1)
                same_rank = 0
            else:
                same_rank += 1

        if check_point == 1:
            ans = i
            break

    if ans >= P:
        print(-1)
    else:
        print(real_rank)

if __name__ == "__main__":
    main()
