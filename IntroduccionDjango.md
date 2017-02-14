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
$ python -m django --version
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
Hasta ahora, lo único que hemos hecho ha sido crear un __proyecto__ Django. Ahora vamos a pasar a crear una __aplicación__. ¿Cuál es la diferencia entre una aplicación y un proyecto? Una aplicación es un módulo que hace algo (por ejemplo, una base de datos, un formulario, etc) y un proyecto es un conjunto de aplicaciones con una configuración concreta para una web en particular. Una app puede estar en varios proyectos y un proyecto puede tener varias apps.

Las apps se suelen hacer de forma modular, para que puedan ser reusables. Aunque no hay nada definido en cuanto a cómo dividir un proyecto en apps, hay [discusiones](http://stackoverflow.com/questions/4879036/django-projects-vs-apps) sobre el tema en la red.

### Ejercicio
__Crea una aplicación para tu proyecto Django. ¿Qué parámetros hay que pasarle al script `manage.py` para ello?__

## La configuración de nuestro proyecto
El fichero `settings.py` de nuestro proyecto tiene todos los parámetros de [configuración](https://docs.djangoproject.com/en/1.10/ref/settings/) de nuestro proyecto. Por ejemplo, incluye el gestor de base de datos que Django usará en nuestra aplicación. Por defecto es __SQLite3__ pero si vas a hacer un proyecto más serio, se recomienda usar otro cliente. En la documentación encontrarás información sobre cómo [instalar una base de datos](https://docs.djangoproject.com/en/1.10/topics/install/#database-installation).

### Ejercicio
__Modifica el fichero `settings.py` con la configuración que necesites para tu proyecto. Consulta la documentación para saber los valores que puede tomar cada parámetro de la configuración.__

En la configuración, podemos añadir las aplicaciones que queramos usar en nuestro proyecto. Por defecto, Django incluye unas cuantas. Algunas de estas aplicaciones usan la base de datos, por lo que debemos crear las tablas en la misma antes de poder usarlas. Para hacer esto, se utilizan las denominadas [migrations](https://docs.djangoproject.com/en/1.10/ref/django-admin/#django-admin-migrate).

### Ejercicio
__¿Cómo se ejecuta una migración en Django? Ejecuta una para poder crear las tablas necesarias para las aplicaciones de nuestro proyecto.__

## Modelos
Imagina que tu aplicación es un blog en el cual los post pueden recibir comentarios de cualquier usuario. En este caso, tendríamos dos elementos principales: un post y un comentario. Estas entidades se representan en Django en forma de __modelos__. Django nos ofrece la facilidad de definir nuestros modelos como si fuesen objetos Python, es decir, mediante clases. Esto es posible debido a que implementa un [__Object-Relational Mapping__](https://en.wikipedia.org/wiki/Object-relational_mapping), una técnica que permite crear tablas de [entidad-relación](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) a partir de objetos.

Para definir los modelos de una aplicación usamos el fichero [`models.py`](https://docs.djangoproject.com/en/1.10/ref/models/instances/#django.db.models.Model) de nuestra aplicación.

### Ejercicio
__Define los modelos necesarios para tu aplicación y aplica una migración a la base  de datos.__ Recuerda que antes de hacer la migración debes añadir la aplicación que creaste a las aplicaciones instaladas del proyecto en el fichero `settings.py` y que antes de hacer la migración sobre el proyecto, debes usar el comando [`makemigrations`](https://docs.djangoproject.com/en/1.10/ref/django-admin/#django-admin-makemigrations) sobre la aplicación.

## Añadiendo datos a nuestra base de datos con la shell de Django
Ejecutando el siguiente comando, podrás entrar a un shell interactivo de Django:

```
$ python manage.py shell
``` 

### Ejercicio
__En la shell de Django, importa los modelos que has creado en el paso anterior y crea varias instancias de las clases modelo. Usa la función `save()` para guardar estos objetos en la base de datos. ¿Cómo podríamos automatizar esta tarea con un script?__

### Ejercicio
**Añade un método `__str__()` a tus modelos para poder imprimir información sobre los mismos en el shell de Django. Consulta en la [documentación](https://docs.djangoproject.com/en/1.10/ref/models/instances/#django.db.models.Model.__str__) qué más métodos puedes crear en los modelos.**

### Ejercicio
__En la [documentación](https://docs.djangoproject.com/en/1.10/topics/db/queries/#field-lookups-intro) nos explican cómo hacer búsquedas en la base de datos. Prueba a hacer diferentes búsquedas usando las funciones `get` y `filter`.__

## Panel de Administración de Django
Una de las aplicaciones instaladas que Django incluye por defecto en los proyectos es [`django.contrib.admin`](https://docs.djangoproject.com/en/1.10/ref/contrib/admin/#module-django.contrib.admin). Esta aplicación nos proporciona un panel de control web de nuestra base de datos. Nos permite añadir y eliminar objetos, entre otras cosas.

Pero para poder acceder al panel de administración, primero debemos crear un superusuario. Esto se hace usando el script python `manage.py`.

Dentro del panel de administración tendremos modelos ya creados: Groups y Users. Estos modelos son creados por otra de las aplicaciones por defecto de Django: [`django.contrib.auth`](https://docs.djangoproject.com/en/1.10/topics/auth/#module-django.contrib.auth).

### Ejercicio
__Crea un super usuario y accede al panel de administración de Django. Recuerda que el panel de administración está en la URL _/admin/_.__

### Ejercicio
__¿Dónde están los modelos que has creado en tu aplicación? Debes añadirlos al panel de administración en el script `admin.py` de tu aplicación. Para ello, debes usar la función `admin.site.register(<modelo>)`, donde `<modelo>` es el modelo que quieres registrar en el panel de administración (recuerda, por tanto, importar tus modelos en el script `admin.py`).__

## Las vistas
Una vista es una "interfaz" entre nuestra aplicación y el archivo HTML que se carga en el navegador. Por ejemplo, si tenemos un blog podemos ir añadiendo entradas al `index.html` de forma manual, aunque llegará un momento en el que sea una tarea muy pesada. Con Django, esto se resuelve de manera muy elegante: mediante plantillas y vistas.

Las vistas se definen en el fichero `views.py` en forma de funciones. Estas funciones tienen dos características especiales:

- Deben devolver o bien un objeto [`HttpResponse`](https://docs.djangoproject.com/en/1.10/ref/request-response/#django.http.HttpResponse) con el contenido que ha sido solicitado o bien lanzar una excepción (por ejemplo, [`Http404`](https://docs.djangoproject.com/en/1.10/topics/http/views/#django.http.Http404)).
- Su primer parámetro es un objeto [`HttpRequest`](https://docs.djangoproject.com/en/1.10/ref/request-response/#django.http.HttpRequest), y corresponde con la petición que ha hecho el navegador para obtener el contenido de la página.

Por ejemplo, si quisiéramos hacer una vista para imprimir el contenido de una entrada de blog concreta usaríamos la siguiente vista:

```python
from django.http import HttpResponse
from .models import BlogEntry

def entrada(request, id):
    texto = BlogEntry.objects.get(entry_id=id)
    return HttpResponse(texto)
```

### Ejercicio
__En el ejemplo anterior no se comprueba si la entrada solicitada existe o no. Crea una vista para tu proyecto, lanzando un error 404 si no existe el contenido solicitado.__

## Plantillas
Una vez hemos definido las diferentes vistas de nuestra aplicación, vamos a hacer una plantilla HTML. Estas plantillas son ficheros HTML normales que colocan llamadas a las vistas con una sintaxis especial. A continuación veremos un ejemplo.

En primer lugar, debemos crear un nuevo directorio llamado _templates_ dentro de nuestra aplicación.

## Las URLs