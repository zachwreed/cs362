import random
from datetime import datetime
# import string

def inputChar():
    return random.choice("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~} ")

def inputString():
    size = random.randint(1, 10)
    return "".join(random.choice("abcdefghijklmnopqrst") for _ in range(size))

def testme():
    tcCount = 0
    state = 0

    while (1):
        tcCount += 1
        c = inputChar()
        s = inputString()
        print("Iteration ", tcCount, ": c = ", c, ", s = ", s, ", state = ", state)

        # if tcCount > 2000:
        #     break

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
        if s == 'reset' and len(s) == 5 and state == 9:
            end = datetime.now()
            # print("Run time:", end - start)
            print("error ")
            exit(200)

def main():
    # random.seed(start)
    testme()

# start = datetime.now()
main()