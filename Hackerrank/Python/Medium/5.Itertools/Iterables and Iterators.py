def comb(n, k):
    if n == k: return 1
    if k == 0: return 1
    if k == 1: return n
    if k > n: return 0

    fac = list()
    fac.append(1)
    fac.append(2)

    for i in range(2, n):
        fac.append(fac[i-1]*(i+1))

    a = fac[n-1]/(fac[k-1]*fac[(n-k-1)])
    return a


def main():
    n = int(input())
    l = input().split()
    k = int(input())

    a = l.count('a')

    all_combi = comb(n, k)
    div_combi = comb(n-a, k)

    print('{:.3f}'.format((all_combi-div_combi)/all_combi))


if __name__ == "__main__":
    # execute only if run as a script
    main()
