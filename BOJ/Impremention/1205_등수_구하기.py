def cmp(a):
    return -a[0]  # 내림차순 정렬

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    new_score = int(data[1])
    P = int(data[2])
    
    vec = []
    for i in range(N):
        num = int(data[3 + i])
        vec.append((num, 0))
    
    vec.append((new_score, 1))
    
    vec = sorted(vec, key=cmp)  # stable_sort 대신 sorted 사용

    ans = 0
    real_rank = 0
    front_score = 0
    same_rank = 0
    iter_vec = iter(vec)
    
    for i, (score, check_point) in enumerate(iter_vec):
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
