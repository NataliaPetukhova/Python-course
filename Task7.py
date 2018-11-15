# Problem 1
def valuesunion(*dicts):
    ans = set()
    for d in dicts:
        for el in d.values():
            ans.add(el)
    return ans


# Problem 2
def subpalindrome(s):
    rev = s[::-1]
    l = len(s)
    while l > 0:
        for i in range(0, len(s) - l + 1):
            half = int(l / 2)
            left = s[i: i + half]
            right = rev[len(s) - (i + l): len(s) - (i + l - half)]
            if left == right:
                return s[i:i + l]
        l -= 1
    return None


# Problem 3
def powers(n, m):
    answ = {}

    def power(n):
        a = 1
        for i in range(n):
            a *= n
        return a

    for i in range(1, n+1):
        answ[i] = power(i) % m
    return answ


# Problem 4
def popcount(n):
    count = 0
    while n > 0:
        count += 1
        n &= n - 1
    return count


# Problem 5
def isIPv4(ip):
    return re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip) != None


# Problem 6
from functools import reduce

def fibonacci(n):
   return functools.reduce(lambda x,n:(x[0]+x[1],x[0]),[(1,1)]*(n-2))[0]

