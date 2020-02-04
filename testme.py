
def inputChar():
    return ' '

def inputString():
    return ''

def testme():
    tcCount = 0
    state = 0

    while (1):
        tcCount += 1
        c = inputChar()
        s += inputString()
        print("Iteration ", tcCount, ": c = ", c, ", s = ", s, ", state = ", state)

        if c == '[' and state == 0:
            state = 1
        if c == '(' and state == 1:
            state = 2
        if c == '{' and state == 2:
            state = 3
        if c == ' 'and state == 3:
            state = 4
        if c == 'a' and state == 4:
            state = 5
        if c == 'x' and state == 5:
            state = 6
        if c == '}' and state == 6:
            state = 7
        if c == ')' and state == 7:
            state = 8
        if c == ']' and state == 8:
            state = 9
        if s[0] == 'r' and s[1] == 'e' and s[2] == 's' and s[3] == 'e' and s[4] == 't' and s[5] == '\0'and state == 9:
            print("error ")
            exit(200)