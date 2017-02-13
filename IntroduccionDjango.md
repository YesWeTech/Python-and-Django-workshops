# Introducción a Django

En este tutorial iremos desarrollando poco a poco una aplicación Django. Cada paso del tutorial explicará un nuevo concepto y en los ejercicios, el alumno aplicará los conceptos explicados para hacer su propia aplicación.

## Instalando Django
Tal y como se indica en la [documentación](https://docs.djangoproject.com/en/1.10/topics/install/#installing-official-release) podemos instalar Django a través de `pip` o a través de github. Lo más sencillo es hacerlo a través de `pip`:

```
$ sudo pip install Django
```

También es importante acostumbrarse a usar [entornos virtuales](https://virtualenv.pypa.io/en/stable/) para no tener problemas por incompatibilidades con distintas versiones de Python/Django.

### Ejercicio
__Instala Django en un entorno virtual creado con `virtualenv`__ (si no tienes `virtualenv` instalado, usa `pip` para instalarlo). __Ten en cuenta que una vez dentro del `virtualenv` no vas a tener que usar `sudo` para poder instalar Django__.

Para ver la versión de Django que tenemos instalada ejecutamos el siguiente comando:

```
python -m django --version
```

Es importante destacar que este tutorial está pensado para __Python 3__. Por tanto, si la versión de Python por defecto en tu sistema operativo es Python2, tendrás que usar `python3` en vez de `python`.

## Creando un proyecto
Una vez tengamos Django instalado en nuestro `virtualenv` pasamos a crear nuestro proyecto. Para ello, debemos usar el comando `django-admin`.

### Ejercicio
__Busca en internet el uso del comando `django-admin` y crea tu proyecto Django en el entorno virtual en el que has instalado Django previamente.__

Una vez tengamos nuestro proyecto creado, Django creará un directorio con los siguientes archivos

* __manage.py__: es un script que nos permite interactuar con nuestra aplicación Django. Puedes consultar más información sobre cómo usarlo en la [documentación](https://docs.djangoproject.com/en/1.10/ref/django-admin/).
* Una carpeta con el __nombre de tu aplicación__: esta carpeta será el paquete Django correspondiente a nuestra aplicación. Suponiendo que nuestra aplicación se llama _miapp_, dentro tendremos:
  * __miapp/__init.py__: Un fichero vacío que sólo sirve para que Python sepa que esta carpeta es un paquete Python.
  * __miapp/settings.py__: Fichero con la configuración de nuestro proyecto Django. Tienes más información sobre la configuración de Django en la [documentación](https://docs.djangoproject.com/en/1.10/topics/settings/).
  * __miapp/urls.py__: Fichero que contiene expresiones regulares correspondientes a las distintas URLs de nuestra aplicación. Esto es algo que veremos más adelante en el tutorial pero que podéis consultar en la [documentación](https://docs.djangoproject.com/en/1.10/topics/http/urls/).
  * __miapp/wsgi.py__: Script python que contiene un pequeño servidor web para realizar pruebas. Este servidor sólo sirve para desarrollar y depurar nuestra aplicación y, para ponerla en producción debemos pasar a usar un servidor _Apache_, _ngix_, etc.

## ¡Hola mundo!
Para verificar que nuestra aplicación funciona,