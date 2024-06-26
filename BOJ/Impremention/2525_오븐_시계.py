# -*- coding: utf-8 -*-
A, B = map(int, input().split())  # map 함수란 주어진 함수와 반복 가능한 객체를 인자로 받아 해당 함수가 모든 요소에 적용된 결과를 반환하는 함수임
C = int(input())

total = B + C

share = total // 60  # 정수 나눗셈 # /은 실수형으로 나옴
remainder = total % 60

A=A+share
B=remainder
A= A%24
print(A, B)