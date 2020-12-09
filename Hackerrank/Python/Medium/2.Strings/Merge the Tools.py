def merge_the_tools(string, k):
    # your code goes here
    num = len(string)//k
    for i in range(num):
        word = string[i*k:i*k+k]
        nword = ""
        fword = ""
        for i in word:
            if i not in fword:
                nword += i
            fword += i
        print(nword)