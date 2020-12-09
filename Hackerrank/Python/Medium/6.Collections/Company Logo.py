#!/bin/python3
import collections as coll


def main():
    name = input()

    f = coll.Counter(sorted(name))
    for i in range(3):
        print(*f.most_common()[i])

if __name__ == "__main__":
    # execute only if run as a script
    main()
