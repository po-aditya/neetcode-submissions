from typing import List

def read_integers() -> List[int]:
    get = input()
    s = get.split(",")
    count = 0
    for i in s:
        s[count] = int(i)
        count += 1
    return s

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
