def add_two_numbers() -> int:
    get = input()
    s = get.split(",")
    counter = 0
    for i in s:
        s[counter] = int(i)
        counter += 1
    sum = 0
    for i in s:
        sum += i
    return sum


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
