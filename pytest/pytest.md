# Introducción a Python - pytest
Una de las fases más importantes del desarrollo, a veces un tanto olvidada, es el __testing__. En la fase de testing, se comprueba que nuestro código funciona correctamente. Es cierto que esto se puede hacer a mano, pero automatizar los tests nos ayuda a comprobar todo de una forma mucho más rigurosa y, además, nos ahorra bastante tiempo.

Hay herramientas para testing en cualquier lenguaje pero en Python, una de las más usadas es [`pytest`](https://docs.pytest.org/en/latest/).

Para instalar `pytest`, hay que hacerlo a través de `pip`:

```shellsession
$ pip install -U pytest
```

Una vez instalado, comprobamos que se ha instalado correctamente:

```shellsession
$ pytest --version
This is pytest version 3.2.5, imported from c:\users\marta\appdata\local\programs\python\python36-32\lib\site-packages\pytest.py
```

## Escribiendo nuestro primer test
Imagina una función que, dado un número, devuelve dicho número multiplicado por dos.

```python
def multiplica_por_dos(x):
    return x*2
```

Una primera aproximación para testear esto sería llamar a la función varias veces con distintos números y comprobar que funciona correctamente.

```python
>>> multiplica_por_dos(5)
10
>>> multiplica_por_dos(10)
20
>>> multiplica_por_dos(2)
4
>>> multiplica_por_dos(50)
100
```

Otra aproximación para testearla sería definir una función que hiciese dichos tests por nosotros. Para ello, usamos la instrucción `assert`, que sirve para asegurar que una determinada condición se cumple. En caso de que la condición no se cumpla, se lanza una excepción del tipo `AssertionError`.

```python
def test_multiplica_por_dos():
    assert multiplica_por_dos(5) == 10
    assert multiplica_por_dos(10) == 20
    assert multiplica_por_dos(2) == 4
    assert multiplica_por_dos(50) == 100
```

Una vez tenemos nuestros tests escritos, los ejecutamos con `pytest`:

```
$ pytest
============================= test session starts =============================
platform win32 -- Python 3.6.3, pytest-3.2.5, py-1.5.2, pluggy-0.4.0
rootdir: C:\Users\Marta\Documents\Github\Women-In-Django\pytest, inifile:
plugins: django-3.1.2
collected 1 item

test_multiplicar.py .

========================== 1 passed in 0.05 seconds ===========================
```

Dado un directorio, `pytest` ejecuta todos los scripts python cuyo nombre sea de la forma `test_*.py` o `*_test.py`. Dentro de dichos archivos, es capaz de encontrar funciones cuyo nombre sea de la foram `test_*` o `*_test` o funciones que estén dentro de una clase cuyo nombre empiece por `Test` (https://docs.pytest.org/en/latest/goodpractices.html#test-discovery).
