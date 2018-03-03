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
  * __miapp/\_\_init\_\_.py__: Un fichero vacío que sólo sirve para que Python sepa que esta carpeta es un paquete Python.
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

## Views
Django sigue una arquitectura similar al tradicional [MVC](https://es.wikipedia.org/wiki/Modelo%E2%80%93vista%E2%80%93controlador), pero con algunas peculiaridades que lo hacen más fácil de modularizar, para poder reutilizar sus componentes más fácilmente. Esta arquitectura, se denomina __MVT (*model*, *view*, *template*)__. En comparación con el MVC original, los views corresponderían con los controladores, y las plantillas con las vistas. 

Los views, son funciones (aunque también se pueden construir con clases) encargadas de convertir un [`HttpRequest`](https://docs.djangoproject.com/en/1.10/ref/request-response/#django.http.HttpRequest) (petición web) en un [`HttpResponse`](https://docs.djangoproject.com/en/1.10/ref/request-response/#django.http.HttpResponse) (respuesta web). Para orquestar este funcionamiento, es necesario un listado de "urls" para que el dispatcher sepa qué función debe aplicar a cada petición, según la URL que esta contenga. 

Además de construir una respuesta, cada view puede tener efectos colaterales sobre el sistema, como por ejemplo, la creación de nuevos objetos en la BD o la modificación de objetos ya existentes. En cualquier caso, los views siempre devolverán una respuesta HTTP. Esta no tiene por qué ser un fichero HTML, sino cualquier tipo de fichero (CSS, JS, JSON, XML...).

Por ejemplo, si quisiéramos hacer una vista para imprimir el contenido de una entrada de blog concreta usaríamos la siguiente vista:

```python
from django.http import HttpResponse
from .models import BlogEntry

def entrada(request, id):
    texto = BlogEntry.objects.get(entry_id=id)
    return HttpResponse(texto)
```

### Ejercicio
__Modifica el ejemplo anterior usando los _shortcuts_ de Django: [`render`](https://docs.djangoproject.com/en/1.10/topics/http/shortcuts/#django.shortcuts.render) y [`get_object_or_404`](https://docs.djangoproject.com/en/1.10/topics/http/shortcuts/#django.shortcuts.get_object_or_404).__ 

### Ejercicio
__Crea una vista para tu proyecto, lanzando un error 404 si no existe el contenido solicitado.__


## Templates
Una vez hemos definido las diferentes vistas de nuestra aplicación, vamos a hacer una plantilla HTML. Estas plantillas son ficheros HTML normales que colocan llamadas a las vistas con una sintaxis especial. Para ver ejemplos de plantillas Django puedes consultar la [documentación](https://docs.djangoproject.com/en/1.10/ref/templates/language/). También es importante que consultes las [etiquetas y filtros que Django incorpora en las plantillas](https://docs.djangoproject.com/en/1.10/ref/templates/builtins/).

Para definir una plantilla, en primer lugar debemos crear un nuevo directorio llamado _templates_ dentro de nuestra aplicación y, dentro del directorio templates debemos crear otro directorio con el nombre de nuestra aplicación. Dentro de este último directorio se encontrará nuestra plantilla HTML. Por tanto, siguiendo con el ejemplo del blog, tendríamos la siguiente estructura de directorios:

```
blog
	|___ templates
		|___ blog
			|__ index.html
```

El parámetro [`TEMPLATES`](https://docs.djangoproject.com/en/1.10/ref/settings/#std:setting-TEMPLATES) del `settings.py` de nuestro proyecto describe cómo Django busca y carga los templates. Por defecto, la opción [`APP_DIRS`](https://docs.djangoproject.com/en/1.10/ref/settings/#std:setting-TEMPLATES-APP_DIRS) es verdadera, lo que significa que Django buscará plantillas en el directorio `templates` de cada aplicación instalada. Debido a este funcionamiento, podemos referinos a nuestro `index.html` simplemente como `blog/index.html` en Django.

¿Por qué es necesario crear un directorio con el nombre de la aplicación dentro del directorio `templates`? Es debido al __Template namespacing__. Si tenemos dos aplicaciones instaladas y ambas tienen una plantilla con el mismo nombre, Django no sabrá distinguir cuál es cuál y, por tanto, cogerá el primer template que encuentre. Para poder distinguir los templates entre aplicaciones, lo más sencillo es colocar los templates de cada aplicación dentro de un directorio con el nombre de la aplicación.

### Ejercicio
__Define una plantilla `index.html` básica para tu proyecto usando elementos del _Django Template System. Pon los enlaces usando la etiqueta [`url`](https://docs.djangoproject.com/en/1.10/ref/templates/builtins/#url).___

## Las URLs
¿Cómo sabe Django cuando un navegador solicita un determinado contenido? Usando la `URLconf`. Cada vista necesita tener asociada una URL para poder ejecutarse. 

Las URLs se definen en el archivo `urls.py` de nuestra aplicación dentro de una __lista__ llamada `urlpatterns`.

Para definir una URL se utiliza la función [`url`](https://docs.djangoproject.com/en/1.10/ref/urls/#django.conf.urls.url) que toma como parámetros una __expresión regular__ que define la URL y la vista para la cual estamos definiendo la URL. Como parámetros opcionales tenemos `kwargs` [para pasar parámetros extra](https://docs.djangoproject.com/en/1.10/topics/http/urls/#views-extra-options) y `name` para [darle un nombre a la URL](https://docs.djangoproject.com/en/1.10/topics/http/urls/#naming-url-patterns).

¿Recuerdas que el panel de administración de administración estaba en la URL _/admin/_? Esto es debido a que su URL se ha definido de la siguiente forma:

```python
url(r'^admin/', admin.site.urls)
```

### Expresiones regulares
Las expresiones regulares que usamos para definir URLs no deben de ser muy complicadas, todo lo contrario, debemos intentar que sean lo más simple posibles. Las reglas para expresar patrones más básicas son:

* `^` para empezar un texto.
* `$` para finalizar un texto.
* `\d` para los dígitos.
* `+` para indicar que el item que precede el símbolo `+` se repetirá más de una vez. Por ejemplo, la expresión regular `^(\d+)` nos indica que hay uno o más dígitos.
* `()` para encapsular parte del patrón.

Volviendo al ejemplo del blog, podríamos definir la URL de un blog de la siguiente forma

```python
url(r'^post/(\d+)/$', views.post)
```

Así, cada post tendría asociado un número y para acceder a ellos, sólo tendríamos que usar una URL con dicho número.

### Ejercicio
__Define las URLs de las vistas que has definido en tu aplicación en el fichero `urls.py` de tu aplicación. Después, incluye las URLs de tu aplicación en el fichero `urls.py` de tu proyecto usando la función [`include`](https://docs.djangoproject.com/en/1.10/ref/urls/#django.conf.urls.include).__

Te habrás dado cuenta que para incluir las URLs de la aplicación `admin` no ha sido necesario usar la función `include`. Esta es la única excepción, siempre que quieras referencias otros URLconfs debes usar esta función.

## ¿Por dónde seguir?
En este taller has aprendido a hacer lo básico con Django, pero aún queda mucho más por hacer. Te dejamos una serie de enlaces interesantes para que puedas seguir ampliando tus conocimientos:

* [La aplicación `django.contrib.auth` para trabajar con usuarios](https://docs.djangoproject.com/en/1.10/topics/auth/)
* [Formularios en Django](https://docs.djangoproject.com/en/1.10/topics/forms/)
* [Awesome Django](http://awesome-django.com/)
* [Django packages](https://djangopackages.org/)