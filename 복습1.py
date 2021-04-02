height = 100
bounce = 3 / 5
num = 1

while num <= 10:
    print(num, round(height * bounce,4))
    height = height * bounce
    num = num + 1

