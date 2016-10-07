# -*- coding: utf-8 -*-

from expects import *
from fizzbuzz import *

results = {
    1: 1,
    2: 2,
    3: "Fizz",
    5: "Buzz",
   15: "FizzBuzz",
   18: "Fizz",
   19: 19,
   20: "Buzz",
   60: "FizzBuzz",
}
 
with describe('Fizzbuzz'):
    with context('when saying calling fizzbuzz'):
        with it('returns list of results'):
            result = fizzbuzz()
            result_yield = list(fizzbuzz_yield())
            
            for counter, expected in results.items():
                expect(result[counter-1]).to(equal(expected))
                expect(result_yield[counter-1]).to(equal(expected))
