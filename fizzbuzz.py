# -*- coding: utf-8 -*-
import time
import timeit
import sys

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

def fizzbuzz_yield(limit=100):
    for i in range(1, limit + 1):
        if not i % 3 and not i % 5:
            n = "FizzBuzz"
        elif not i % 3:
            n = "Fizz"
        elif not i % 5:
            n = "Buzz"
        else:
            n = i
        yield n
         

if __name__ == "__main__":
    for limit in (100, 1000000, 100000000):
        start = time.time()
        #timeit.timeit(fizzbuzz(limit))
        fizzbuzz_yield(limit)
        print "fizzbuzz_yield with ",limit,": ", (time.time() - start)
        fizzbuzz(limit)
        print "fizzbuzz (list) with ",limit,": ", (time.time() - start)
        print "--"
        raw_input()
