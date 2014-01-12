#Práctica 3

Rafael Carrasco Ruiz

Licencia GNU GENERAL PUBLIC LICENSE Version 3 


##Introducción

Vamos a crear una máquina virtual con VirtualBox utilizando dos sistemas operativos, Ubuntu Server y Fedora. Una vez instalados ambos sistemas operativos, vamos a ir cambiando de a distintas configuraciones de la máquina virtual para comprobar cual de ellas es la más optima.

En cada una montaremos un ejemplo parecido al usado en prácticas anteriores. Un sencillo programa desarrollado en Python y utilizando Pymongo para base de datos.

Comprobaremos el rendimiento de las distintas configuraciones con Apache Benchmark.


##Instalación VirtualBox

Descargamos el paquete de la pag. https://www.virtualbox.org/wiki/Linux_Downloads

Después realizamos la instalación.

  ![instalacion](https://dl.dropbox.com/s/68p29yt0eux56w5/virtual.png)
  

Una vez tenemos VirtualBox instalado y en funcionamiento, empezamos con la instalación de los Sistemas Operativos:

  Ubuntu Server
  
  ![Ubuntu](https://dl.dropbox.com/s/f1gu5vsoave6hu5/instSOUb.png)
  

Para poder utilizar los ejemplos tenemos que instalar los paquetes de Python, Webpy y Pymongo para su correcto funcionamiento.
  
  ![webpy](https://dl.dropbox.com/s/1spebp2m8gesyb5/webpyUbu.png)
  
  ![mongo](https://dl.dropbox.com/s/mqkwapnsaf5kxq7/mongo.png)
  
Una vez instalados todos los paquetes, mediante scp pasamos los documentos de nuestro ejemplo a nuestra máquina virutal y comprobamos que todo funciona correctamente.

  Ejecutamos la web con el propio servidor que nos proporciona webpy y vemos que todo funciona.
  
  `python practica3.py`
  
  ![python](https://dl.dropbox.com/s/obdizkarwr6y3s3/correct.png)
  
  Y accedemos.
  
  ![web](https://dl.dropbox.com/s/au5b4jjizf42dvz/funciona.png?m=)
  

Realizamos los mismo pasos con Guadalinex.

Guadalinex v8
  
  ![Guada](https://dl.dropbox.com/s/wkju96yavmjbue2/instguada.png)
  
Y comprobamos que funciona correctamente.

  ![guadafu](https://dl.dropbox.com/s/gy7l9au5wu60kzv/guadfun.png)

##Configuración máquinas virtuales

1º. Configuración
    
    Sistema Operativo: Ubuntu server 12.04
    Procesador: 1 proc.
    Ram: 256 MB
  
2º. Configuración

    Sistema Operativo: Ubuntu server 12.04
    Procesador: 2 proc.
    Ram: 512 MB

3º. Configuración

    Sistema Operativo: Ubuntu server 12.04
    Procesador: 2 proc.
    Ram: 1 GB

4º. Configuración

    Sistema Operativo: Guadalinex v8
    Procesador: 1 proc.
    Ram: 256 MB

5º. Configuración

    Sistema Operativo: Guadalinex v8
    Procesador: 2 proc.
    Ram: 512 MB

6º. Configuración

    Sistema Operativo: Guadalinex v8
    Procesador: 2 proc.
    Ram: 1 GB
  
##Apache Benchmark
Para el análisis utilizamos Apache Benchmark, herramienta para la evaluación comparativa del Protocolo de transferencia de hipertexto servidor Apache (HTTP).

Con una carga de 1000 peticiones y 100 solicitudes concurrentemente.

 ![bench](https://dl.dropbox.com/s/5v92gsd50fanius/bench.png)

##Resultados


Configuracion 1: 

  1 nucleo, 256 MB, ubutu Server

<table>
    <tr>
        <td>Request per second</td>
        <td>Time per request</td>
        <td>Time per request (mean, across all concurrent requests)</td>
    </tr>
    <tr>
        <td>37.55 seg</td>
        <td>2662,943 ms</td>
        <td>26,629 ms</td>
    </tr>
</table>


Datos analizados:

* Request per second = peticiones atendidas por segundo
* Time per request = tiempo medio que el servidor tarda en atender peticiones concurrentes
* Time per request (mean, across all concurrent requests) = tiempo medio que el servidor tarda en atender una petición



