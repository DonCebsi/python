# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def main():
    ab = int(input())
    bc = int(input())

    ac = math.sqrt(math.pow(ab,2) + math.pow(bc, 2))

    mbc = round(math.degrees(math.acos(bc/ac)))

    print(''.join([str(mbc), '°']))

if __name__ == "__main__":
    # execute only if run as a script
    main()

'''
10
10
'''
