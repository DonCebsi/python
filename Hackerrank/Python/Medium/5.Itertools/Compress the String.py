from itertools import groupby
if __name__ == '__main__':
    num = input()
    groups = []
    for i, j in groupby(num):
        groups.append((len(list(j)), int(i)))
    print(*groups)
