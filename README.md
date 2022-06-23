# Test-Unicenpython
Prueba Automatizada de llenado de formulario de solicitud de informacion para una determianda carrera en la UNICEN.  

Esta es una prueba de Automatizacion de llenado de un formulario de solicitud de informacion para una determinada carrera en la UNICEN, esta prueba, fue escrita en el lenguaje de Programacion Python. Para su Ejecucion, Necesitara tener instalado como minimo el navegador Google Chrome y contar con una conexion a internet.

Pasos de Instalacion de herramientas requeridas para la ejecucion del Archivo: "unicen.py"

Instalacion de python en su ultima version, en caso de presentar errores instale python en la version 3.10.4 (Para mas informacion de como instalar dependiendo su sistema operativo ademas de recursos para su instalacion, visite: https://www.python.org/) Link para la descarga (en Windows 10): https://www.python.org/downloads/

Una vez completada la instalacion de python, instale pip (Sistema de gestion de paquetes en python), para saber como instalar pip de acuerdo a su sistema operativo, visite: https://tecnonucleous.com/2018/01/28/como-instalar-pip-para-python-en-windows-mac-y-linux/ Alli encontrara toda informacion necesaria sobre como instalar pip de acuerdo a su eleccion y a su sistema operativo.

Una vez instalado pip, descargue el archivo "unicen.py" (Guardelo en una carpeta separada)

En la carpeta que contiene el archivo "unicen.py" abra una terminal (Consola de comandos)

Ejecute el comando "pip install -U selenium"

Una vez Terminada la instalacion de selenium (Culminacion de ejecucion del anterior comando), Ejecute el siguiente comando Ahora: "pip install pandas"

Una vez terminada la instalacion de pandas (Culminacion de ejecucion del anterior comando), abra su navegador google Chrome

Dirijase a la parte superior derecha y localice la opcion de "Mas" (tambien puede ser 3 puntos colocados de manera vertical) haga click alli

En el menu que surge haga click en "Ayuda"

Surgira un nuevo menmu de sub-opciones, elija: Informacion de Google Chrome

Se le mostrara la version de su Google Chrome.

Dirijase al sitio web:"https://chromedriver.chromium.org/downloads"

Busque entre las opciones de la pagina una version que se adapte a su version y haga click en el enlace correspondiente.(considere los 3 primeros numeros de su version instalada para una busqueda rapida en la pagina)

Se le mostraran las opciones correspondientes para cada sistema operativo, elija el adecuado para su sistema operativo y haga click en el enlace correspondiente y guarde el archivo.

Una vez descargado el archivo, este sera un zip, utilizando una herramienta de descompresion, descomprima el archivo.zip

Dependiendo de la herramienta que use para descomprimir el archivo, se le puede generar una carpeta con el mismo nombre del archivo zip, ingrese a la carpeta(de no ser asi, ignore este paso)

El archivo en cuestion tiene por nombre:"chromedriver", copie la ruta (directorio) de donde se encuentra el archivo "chromedriver"

Donde haya descargado el archivo "unicen.py" abra el archivo "unicen.py"(no lo ejecute, utilice un editor de archivos, Ejemplo: Visual Studio Code)

En la linea: "driver_path = " (sin borrar los parentesis y las comillas simplres a continuacion) elimine la ruta incluida al momento de descargar, y pegue el directorio (ruta) de su chromedriver.

Abra una linea (Consola) de comandos (Donde se encuentre el archivo "unicen.py") y ejecute el comando: "python unicen.py"


Se ejecutara el archivo "unicen.py" esto es lo que sucedera:

Se abrira un navegador google chrome y se auto-ajustara al tamaño de su pantalla(El tamaño sera de su pantalla completa)

Abrira la pagina principal de UNICEN

se llenara el formulario de Solicitu de informacion

se hara click en el boton de "Sign in"

Se enviara el formulario y se refrescara la pagina mostrando un poco antes del formulario de solicitud de informacion un mensaje indicando que los datos fueron enviados correctamente.

al pasar unos segundos la ventana (Navegador google Chrome) que se abrio, se cerrara.

Powered By Josué Rodrigo Chura Rojas :-)
