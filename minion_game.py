def minion_game(s):
    Stuart=0
    Kevin=0
    vowel='AEIOU'
    for i in range(len(s)):
        if s[i] in vowel:
            Kevin+=len(s)-i
        else:
            Stuart+=len(s)-i
    if Stuart>Kevin:
        print("Stuart "+"%d" %Stuart)
    elif Kevin>Stuart:
        print("Kevin "+"%d" %Kevin)
    else:
        print("Draw")


s=input()
minion_game(s)