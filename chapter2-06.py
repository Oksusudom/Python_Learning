num = 0

while True:
    num = int(input())

    if num % 4 != 0:
        print('평년')
    elif num % 100 != 0:
        print('윤년')
    elif num % 400 == 0:
        print('윤년')
    else :
        print('평년')