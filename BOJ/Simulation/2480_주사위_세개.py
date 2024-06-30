
# -*- coding: utf-8 -*-


def main():
    num1,num2,num3=map(int,input().split())

    if num1 == num2:
        if num2 == num3:
            print(10000+num1*1000)
            return
        if num2 !=num3:
            print(1000+num1*100)
            return
    elif num2 == num3:
        print(1000+num2*100)
        return
    elif num1 == num3:
        print(1000+num1*100)
        return
    else:
        largest = max(num1,num2,num3)
        print(largest*100)
        return


if __name__ == "__main__":
    main()
    