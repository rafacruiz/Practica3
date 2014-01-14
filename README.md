#Práctica 3

Rafael Carrasco Ruiz

Licencia GNU GENERAL PUBLIC LICENSE Version 3 


##Introducción

Vamos a crear una máquina virtual con VirtualBox utilizando dos sistemas operativos, Ubuntu Server y Guadalinex v8. Una vez instalados ambos sistemas operativos, vamos a ir cambiando de a distintas configuraciones de la máquina virtual para comprobar cual de ellas es la más optima.

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
  

Realizamos los mismos pasos con Guadalinex.

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

  1 nucleo, 256 MB, ubuntu Server

<table>
    <tr>
        <td>Request per second</td>
        <td>Time per request</td>
        <td>Time per request (mean, across all concurrent requests)</td>
    </tr>
    <tr>
        <td>37.55 / seg</td>
        <td>2662,943 ms</td>
        <td>26,629 ms</td>
    </tr>
</table>

Configuracion 2: 

  2 nucleo, 512 MB, ubuntu Server

<table>
    <tr>
        <td>Request per second</td>
        <td>Time per request</td>
        <td>Time per request (mean, across all concurrent requests)</td>
    </tr>
    <tr>
        <td>39.37 / seg</td>
        <td>2539,826 ms</td>
        <td>25,398 ms</td>
    </tr>
</table>

Configuracion 3: 

  2 nucleo, 1 GB, ubuntu Server

<table>
    <tr>
        <td>Request per second</td>
        <td>Time per request</td>
        <td>Time per request (mean, across all concurrent requests)</td>
    </tr>
    <tr>
        <td>27.50 / seg</td>
        <td>3635,960 ms</td>
        <td>36,360 ms</td>
    </tr>
</table>

Configuracion 4: 

  1 nucleo, 256 MB, Guadalinex v8

<table>
    <tr>
        <td>Request per second</td>
        <td>Time per request</td>
        <td>Time per request (mean, across all concurrent requests)</td>
    </tr>
    <tr>
        <td>23.04 / seg</td>
        <td>4340,220 ms</td>
        <td>43,402 ms</td>
    </tr>
</table>

Configuracion 5: 

  2 nucleo, 512 MB, Guadalinex v8

<table>
    <tr>
        <td>Request per second</td>
        <td>Time per request</td>
        <td>Time per request (mean, across all concurrent requests)</td>
    </tr>
    <tr>
        <td>21.15 / seg</td>
        <td>4729,185 ms</td>
        <td>47,292 ms</td>
    </tr>
</table>

Configuracion 6: 

  2 nucleo, 1 GB, Guadalinex v8

<table>
    <tr>
        <td>Request per second</td>
        <td>Time per request</td>
        <td>Time per request (mean, across all concurrent requests)</td>
    </tr>
    <tr>
        <td>22.75 / seg</td>
        <td>4394.899 ms</td>
        <td>43.949 ms</td>
    </tr>
</table>

Datos analizados:

* Request per second = peticiones atendidas por segundo
* Time per request = tiempo medio que el servidor tarda en atender peticiones concurrentes
* Time per request (mean, across all concurrent requests) = tiempo medio que el servidor tarda en atender una petición

##Conclusión

Como podemos observar en los resultados, las dos más eficientes hablando de tiempo de respuesta son la primera configuración (Ubuntu server) y la cuarta configuración (Guadalinex v8), ambas configuraciones más bajas hablando de hardware. Como podemos ver en la primera configuración el tiempo de peticiones atendidas por segundo es la intermedia de las tres de Ubuntu server, pero es la configuración más baja y con un tiempo medio bajo en atender el servidor una petición.

Y la cuarta configuración (Guadalinex v8) pasa algo parecido con la primera configuración. Tiene el mayor número de peticiones atendidas por segundo y el tiempo medio que el servidor tarda en atender una petición más bajo y con la configuración hardware más baja.




