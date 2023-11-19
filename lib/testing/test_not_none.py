#!/usr/bin/env python3

from not_none_functions import return_not_none

def test_return_not_none():
    '''in not_none_functions, function "return_not_none" returns a value that is not None.'''
    assert return_not_none() is not None, 'return_not_none() should not return None'
#   assert 'return_not_none' == return_not_none(), 'return_not_none() should return "return_not_none"'
