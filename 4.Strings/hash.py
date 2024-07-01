if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    ab=tuple(integer_list)
    print(ab)
    ba=hash(ab)
    print(ba)