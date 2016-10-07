# -*- coding: utf-8 -*-


def fizzbuzz(limit=100):
    res = []
    for i in range(1, limit + 1):
        if not i % 3 and not i % 5:
            res.append("FizzBuzz")
        elif not i % 3:
            res.append("Fizz")
        elif not i % 5:
            res.append("Buzz")
        else:
            res.append(i)
    return res
         

if __name__ == "__main__":
    print fizzbuzz()
