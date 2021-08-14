if __name__ == '__main__':
    s = input()
    isalpha=0
    islower=0
    isupper=0
    isalnum=0
    isdigit=0
    for i in range(len(s)):
        if(s[i].isalpha()):
            isalpha=1
            if s[i].islower():
                islower=1
            if s[i].isupper():
                isupper=1
        if s[i].isalnum():
            isalnum=1
            if s[i].isdigit():
                isdigit=1  
    if isalpha==1:
        print(True)
    else:print(False)
    if isalnum==1:
        print(True)
    else:print(False)
    if isdigit==1:
        print(True)
    else:print(False)
    if islower==1:
        print(True)
    else:
        print(False)
    if isupper==1:
        print(True)
    else:print(False)
            