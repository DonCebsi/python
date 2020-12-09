def main():
    n, m = input().split()

    numbers = [int(x) for x in input().split()]

    a = set([int(x) for x in input().split()])
    b = set([int(x) for x in input().split()])

    count = [0 + 1 if x in a else 0 - 1 if x in b else 0 + 0 for x in numbers]

    print(sum(count))



if __name__ == "__main__":
    # execute only if run as a script
    main()
