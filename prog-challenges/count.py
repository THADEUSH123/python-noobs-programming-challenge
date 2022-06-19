

def split(l):
    for i in range(0,len(l)):
        if sum(l[0:i]) == sum(l[i:]):
            return (l[0:i], l[i:])
    return l


lst = [1,3,4,6,2,0,0]
print(split(lst))


def count(c, string):
    # Count variable
    res = 0
    for i in string:
        # Checking character in string
        if i == c:
            res += 1
    return res


print(count("l", "hello world"))

def count2(c, string) :

    # Count variable
    res = 0
    for i in range(len(string)):

        # Checking character in string
        if (string[i] == c):
            res = res + 1
    return res

print(count("l", "hello world"))
