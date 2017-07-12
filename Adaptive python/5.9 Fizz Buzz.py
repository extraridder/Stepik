def check_(x):
    if x % 15 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)



tmp_ = list(input().split(" "))
x = tmp_[0]
y = tmp_[1]
for each in range(int(x), int(y) + 1):
    check_(each)