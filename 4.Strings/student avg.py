import math
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    num=student_marks[name]
    d=0
    for i in num:
        d=d+i
        print(d)
    avg=d/len(scores)
    print(math.floor(avg))