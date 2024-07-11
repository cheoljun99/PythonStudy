# -*- coding: utf-8 -*-


def main():
    while True:
        try:
            st=str(input().strip())
            print(st)
            
        except EOFError:
            break
    return



if __name__ == "__main__":
    main()
    