# -*- coding: utf-8 -*-

from expects import *
from fizzbuzz import *

results = {
    1: 1,
    2: 2,
    3: "Fizz",
    5: "Buzz",
   15: "FizzBuzz",
}
 
with describe('Fizzbuzz'):
    with context('when saying calling fizzbuzz'):
        with it('returns list of results'):
            result = fizzbuzz()
            
            for counter, expected in results.items():
                expect(result[counter-1]).to(equal(expected))
