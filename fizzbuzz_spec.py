# -*- coding: utf-8 -*-

from expects import *

from fizzbuzz import fizzbuzz


with describe('Fizzbuzz'):
    with context('when running the test'):
        with it('says hello'):
            name = 'Foo'
            
            result = say_hello(name)
            
            expect(result).to(equal('Hello Foo'))
