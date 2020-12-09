from collections import deque


def main():
    d = deque()
    for _ in range(int(input())):
        num_cubes = int(input())
        cubes = input().split()
        smol = int(cubes[0])

        for cube in cubes:
            d.append(int(cube))
            if int(cube) < smol:
                smol = int(cube)
        smol_pos = d.index(smol)
        ret = "Yes"

        last = d[0]
        for i in range(smol_pos):
            current = d.popleft()
            if current > last:
                ret = "No"
                break
            last = current

        last = d[-1]
        for i in range(len(d)-1):
            current = d.pop()
            if current > last:
                ret = "No"
                break
            last = current

        d.clear()
        print(ret)

    print(*d)




if __name__ == "__main__":
    # execute only if run as a script
    main()
