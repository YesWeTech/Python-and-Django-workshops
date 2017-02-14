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
Para verificar que nuestra aplicación funciona, vamos a ejecutar el servidor de pruebas que nos facilita Django. Para ello, usamos el script `manage.py`.

### Ejercicio
__¿Qué parámetros hay que pasarle al script `manage.py` para poder ejecutar el servidor de Django? ¿Y si quieres ejecutar el servidor en un puerto específico?__ Pista: todo está en la [documentación](https://docs.djangoproject.com/en/1.10/ref/django-admin/#django-admin-runserver).

Una vez hayamos ejecutado el servidor, tenemos que abrir la URL que nos indica en consola y veremos un mensaje indicándonos que todo ha funcionado correctamente.

## Creando nuestra primera app
Hasta ahora, lo único que hemos hecho ha sido crear un __proyecto__ Django. Ahora vamos a pasar a crear una __aplicación__. ¿Cuál es la diferencia entre una aplicación y un proyecto? Una aplicación es una aplicación web que hace algo (por ejemplo, una base de datos, un formulario, etc) y un proyecto es un conjunto de aplicaciones con una configuración concreta para una web en particular. Una app puede estar en varios proyectos y un proyecto puede tener varias apps.

### Ejercicio
__Crea una aplicación para tu proyecto Django. ¿Qué parámetros hay que pasarle al script `manage.py` para ello?__

## Las vistas y las URLs
Una vista en Django es una función Python que comunica una app con el template HTML de nuestra web. Con las vistas. Por ejemplo, imagina que nuestra aplicación es una base de datos sobre restaurantes, podríamos añadir restaurantes directamente al fichero HTML de nuestra web, aunque llegará un momento en el que será imposible administrar y añadir nuestros restaurantes. Django nos permite hacerlo de una forma muy sencilla: creando una platilla HTML que se comunica con la aplicación Django y ésta se encarga de poner los restaurantes almacenados en la base de datos. Para realizar esta comunicación, están las vistas.

Las vistas se definen en el fichero `views.py` de nuestra aplicación.

### Ejercicio
__Crea una vista llamada `index` que imprima el siguiente mensaje:__ "hola! esta es mi primera vista".

Antes de ejecutar el servidor para ver nuestro _hola mundo_, debemos configurar la URL que Django debe de usar para llamar a la vista. Para ello, debemos crear un nuevo fichero en nuestra aplicación llamado `urls.py`.

### Ejercicio
__Consulta en la [documentación](https://docs.djangoproject.com/en/1.10/topics/http/urls/) cómo crear una URL para la vista `index` y, a continuación, crea una URL para la misma.__ Ten en cuenta que tendrás que incluir las URLs de tu aplicación en el fichero URLs de tu proyecto (función [include()](https://docs.djangoproject.com/en/1.10/ref/urls/#django.conf.urls.include)).

## La configuración de nuestro proyecto
El fichero `settings.py` de nuestro proyecto tiene todos los parámetros de [configuración](https://docs.djangoproject.com/en/1.10/ref/settings/) de nuestro proyecto. Por ejemplo, incluye el gestor de base de datos que Django usará en nuestra aplicación. Por defecto es __SQLite3__ pero si vas a hacer un proyecto más serio, se recomienda usar otro cliente. En la documentación encontrarás información sobre cómo [instalar una base de datos](https://docs.djangoproject.com/en/1.10/topics/install/#database-installation).

### Ejercicio
__Modifica el fichero `settings.py` con la configuración que necesites para tu proyecto. Consulta la documentación para saber los valores que puede tomar cada parámetro de la configuración.__

En la configuración, podemos añadir las aplicaciones que queramos usar en nuestro proyecto. Por defecto, Django incluye unas cuantas. Algunas de estas aplicaciones usan la base de datos, por lo que debemos crear las tablas en la misma antes de poder usarlas. Para hacer esto, se utilizan las denominadas [migrations](https://docs.djangoproject.com/en/1.10/ref/django-admin/#django-admin-migrate).

### Ejercicio
__¿Cómo se ejecuta una migración en Django? Ejecuta una para poder crear las tablas necesarias para las aplicaciones de nuestro proyecto.__

## Modelos
