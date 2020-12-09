if __name__ == '__main__':
    s = input()
    order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
    print(*sorted(s,key=order.index),sep='')
