def minion_game(string):
    # your code goes here
    winner = ""
    s_points = 0
    k_points = 0
    #banana
    # calculate points
    for i in range(len(string)):
        word = s[i]
        if word in "AEIOU":
            k_points += len(string)-i
        elif not word.isspace():
            s_points += len(string)-i


    # who wins?
    if s_points > k_points:
        print("Stuart %d" % s_points)
    elif s_points < k_points:
        print("Kevin %d" % k_points)
    else:
        print("Draw")

