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

### Más sobre `assert`
`assert` nos permite asegurar que una condición se cumple en nuestro código y lanzar una excepción en caso de que no se cumpla. Esto puede ser muy útil a la hora de validar una entrada.

Imagina una función que debe recibir un DNI. Como sabemos, el DNI tiene 8 números y, al final, una letra. Además, la letra puede ser calculada con un [simple algoritmo](http://www.interior.gob.es/web/servicios-al-ciudadano/dni/calculo-del-digito-de-control-del-nif-nie).

```python
def input_validation_dni(input_dni):
    try:
        assert len(input_dni) == 9, "El DNI introducido no tiene 9 caracteres"
        assert input_dni[:8].isnumeric(), "Los primeros 8 caracteres del DNI no son numéricos"
        assert input_dni[-1].isalpha(), "El último carácter del DNI no es una letra"
    except AssertionError as e:
        print ("ERROR: {}".format(str(e)))
```

Esta función no hace nada si la entrada es correcta, pero imprime un mensaje de error y su razón si la entrada no ha pasado por alguno de los checks. Además, acompañar el check de un mensaje de error nos permite imprimir dicho mensaje después para informar al usuario.

```python
>>> input_validation_dni('12345678a')
>>> input_validation_dni('12345678A')
>>> input_validation_dni('123456780')
ERROR: El último carácter del DNI no es una letra
>>> input_validation_dni('1')
ERROR: El DNI introducido no tiene 9 caracteres
>>> input_validation_dni('a12345678')
ERROR: Los primeros 8 caracteres del DNI no son numéricos
```

### Ejercicio

Un problema muy típico de programación, es el dada una lista de paréntesis, corchetes y llaves, comprobar si se abren y cierran correctamente. Un ejemplo:
- Cadena 1: `()`, `[]`, `{}` -> Correcto.
- Cadena 2: `([{}])`, `{{([{([[[]]])}])}}` -> Correcto.
- Cadena 3: `[{(})]` -> Error.

Una vez visto esto, tu tarea consiste en programar una función para resolver este problema y los tests para esta función. (Consejo: programa primero los tests).


## Profiling con pytest

Una de las muchas posibles pruebas que podemos hacerle a nuestro código o aplicación, es el _profiling_, es decir, saber cómo de eficiente o no es nuestro código. Para ello, pytest nos ofrece distintas herramientas, como son el decorador `timeout` y el parámetro de pytest.

Con el parámetro `durations` podemos lanzar una serie de tests y obtener una lista con las ejecuciones más lentas:

```
$ pytest --durations=10
============================= test session starts =============================
platform win32 -- Python 3.6.4, pytest-3.2.5, py-1.5.2, pluggy-0.4.0
rootdir: C:\Users\Braulio\Documents\Github\Women-In-Django, inifile:
plugins: django-3.1.2
collected 1 item

pytest\test_multiplicar.py .

========================== slowest 10 test durations ==========================
0.00s setup    pytest/test_multiplicar.py::test_multiplica_por_dos
0.00s call     pytest/test_multiplicar.py::test_multiplica_por_dos
0.00s teardown pytest/test_multiplicar.py::test_multiplica_por_dos
========================== 1 passed in 0.05 seconds ===========================
```

Con `timeout`, podemos parar la ejecución de un test pasado _x_ tiempo. Esto nos puede servir para saber si una función excede un tiempo de ejecución, por si queremos hacer una función más eficiente, o bien, para evitar que nuestro test entre en un bucle infinito sin nosotros saberlo, debido a un fallo en un bucle o similar.

Podemos usar `timeout` de dos formas distintas:
- Parámetro de pytest: hacemos una llamada a pytest de la siguiente forma: `pytest --timeout=300`. Esto afecta a todos los tests.
- Decorador de una función: si el el timeout lo queremos aplicar a una función en especial, podemos definir una función con este decorador: `@pytest.mark.timeout(tiempo)`. Esto parará la ejecución de esa función si excede el tiempo que le pongamos, y dará ese test como fallido.
