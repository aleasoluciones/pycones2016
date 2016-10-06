# -*- coding: utf-8 -*-

from expects import *


with describe('Fizzbuzz'):
    with context('when saying hello to Foo'):
        with it('says Hello to Foo'):
            name = 'Foo'
            
            result = say_hello(name)
            
            expect(result).to(equal('Hello Foo'))
