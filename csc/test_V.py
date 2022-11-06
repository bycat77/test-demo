import pytest
def add(x):
    return x*2

def test_add01_int():
    assert 2==add(1)

def test_add02_float():
    assert 2.2 ==add(1.1)

def test_add03_fushu():
    assert -3 ==add(-1.5)

def test_add03_zero():
    assert 0==add(0)