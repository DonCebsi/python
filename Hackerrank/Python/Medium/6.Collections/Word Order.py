# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict


def main():
    occurence = OrderedDict()
    for _ in range(int(input())):
        word = input()
        if word in occurence:
            occurence[word] += 1
            continue
        occurence[word] = 1
    print(len(occurence))
    print(*occurence.values())



if __name__ == "__main__":
    # execute only if run as a script
    main()
