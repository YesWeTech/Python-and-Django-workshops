#!/usr/bin/python

def multiplica_por_dos(x):
    return x*2

def test_multiplica_por_dos():
    assert multiplica_por_dos(5) == 10
    assert multiplica_por_dos(10) == 20
    assert multiplica_por_dos(2) == 4
    assert multiplica_por_dos(50) == 100
