# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools as it

def main():
    k, m = map(int, input().split())
    l = list()

    for i in range(k):
        l.append(map(int,input().split()[1:]))

    total = 0
    for i in it.product(*l):
        big = 0
        for j in i:
            big += (j**2) %m

        big = big%m
        if big > total:
            total = big

    print(total)


if __name__ == "__main__":
    # execute only if run as a script
    main()
