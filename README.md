##Bienvenido a Todo Anime.
En este proyecto podemos encontrar cualquier tipo de anime de acción, autos y mucho más.
#### Inicio de Proyecto desde GitHub:
1. Crear un nuevo repositorio en GitHub.
1. agregarmos modulos **.gitignore** y **README.md**.
1. copiamos link de repositorio **https://github.com/RodrigoTapia21/Entrega-final-Rodrigo-Tapia-.git**
1. Nos vamos al **Visual Studio.**

------------

### Inicio de Proyecto desde Visual Studio:
1. Empezamos abriendo la consola y escribimos: *git clone https://github.com/RodrigoTapia21/Entrega-final-Rodrigo-Tapia-.git*. Con esto conectamos el visual con nuestro repositorio en **GitHub.**
1. django-admin startproject **Proyecto .** <---- *NO HAY QUE OLVIDARSE DEL PUNTO*
1. python manage.py startapp **TodoAnime** <--- *NOMBRE DE NUESTRA APP*
1. Agregamos en **settings.py** el nombre de nuestra app:

------------


**`INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

'EjemploConfig', <-- NOMBRE DE NUESTRA APP 
]`**

------------


1. Hacemos **python manage.py migrate** para crear nuestra primera migración a la base de datos.
1. Creamos la siguiente estructura de carpeta: **Templates/TodoAnime/Registration**
- Dentro de estas carpetas creamos el archivo **index.html**
1. Creamos la siguiente estructura de carpeta:  **Static/TodoAnime/css/js/assets** 
-  En las carpetas **css/js/assets** agregamos los respectivos archivos descargados.

En este punto ya tendriamos todo lo necesario para poder avanzar con los **html** y las **views**

------------


## WORK FLOW:
> Vamos a seguir una serie de pasos que nos van a ayudar a mantener la organizacion de las cosas.:

1. Creamos la **view** que necesitemos.
`
def index(request):
    return render(request, "ejemplo/indexr.html")`
1. Hacemos el **.html** respectivo a la view
*h1>
*Hola esto es el template index*/h1>*

1. Terminamos macheando con la **url **de la view
from django.contrib import admin
from django.urls import path
from ejemplo***<-nombre de nuestra app***.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index , name= 'index'), # ESTA ES LA NUEVA FUNCTION
]
###### Con este WROK FLOW podemos crear view, html y urls correctamente.

------------
## Página web:

- Corremos ***Python manage.py runserver***
- Como se tiene que ver si esta todo bien:
[![](https://kbimages.dreamhosters.com/images/2018-04_django-create-project.png)](http://https://kbimages.dreamhosters.com/images/2018-04_django-create-project.png)

------------


###Pasos para hacer un Push a github: 

Correr en la terminal: **git add .**

Correr en la terminal:**git commit -m "primer commit de mi proyecto"**

Correr en la terminal: **git push origin main**


------------

# TODO ANIME FUNCIONES
###### Inicio con cuenta registrada:
- Tenemos al rededor de 10 funciones diferentes entre las cuales se encuentra:
1. "**Who Mm I"**: Se encuentra información sobre mi y el origen de la página web.
1. "**Home"**: Podemos observar un carousel con 2 fotos y abajo se observan 6 otros con su detalle o actualizacion y borrado si sos dueño.
1. "**All Anime"**: Template donde se encuentran todos los animes con botones de *detalle*, *actualizar* y *borrar*.  *Solo si sos dueño podes actualizar o borrar*.
1. "**Send Message"**: Un template con formulario de envio de mensajes a diferentes usarios registrados.
1. "**My Anime"**: Template solo con los animes ingresados por el usuario dueño. con botones de *detalle*, *actualizar* y *borrar*. 
1. "**Add Anime"**: Template usado para agregar cualquier tipo de anime con *titulo, tipo, descripcion , creador e imagen. * Descargar la foto de google.
1. "**Profile"**: Template con informacion del usuario con *imagen, nombre y red social*.
1. "**message"**: Template donde almacenan los mensajes recibidos de diferentes usuarios con boton para borrar.
1. "**OUT"**: Boton usado para salir de la cuenta del usuario. 

------------
###### pagina sin estar registrado:
1. "**Who Mm I**": Se encuentra información sobre mi y el origen de la página web.
1. "**Home"**: Podemos observar un carousel con 2 fotos y abajo se observan 6 otros con su detalle. Solo se muestra *actualizacion y borrado* si sos dueño registrado.
1. "**All Anime"**: Template donde se encuentran todos los animes con botones de *detalle*, *actualizar* y *borrar*.  *Solo si sos dueño registrado podes actualizar o borrar*.
1. "**Send Message"**: Un template con formulario de envio de mensajes a diferentes usarios registrados.
1. "**Log in"**: Un template para aquellos usuarios que ya se registraron con *usuario y contraseña*.
1. "**SingUp"**: Template para registrarse como usuario, te pide agregar tu *nombre y confirmar 2 veces tu contraseña.*

------------

### Search
- Metodo de busqueda para encontrar el anime que quieras, funciona con **boton** o apretando la tecla **enter.**

------------

