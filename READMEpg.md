# MCOC2020-P0
# Entrega 1: Mi computador

* Marca/modelo: Lenovo ideapad 330S-14IKB
* Tipo: Notebook
* Año Adquisición: 2019
* Procesador:
  * Marca/Modelo: Intel Core i5-8250U CPU
  * Velocidad Base: 1.6 GHz
  * Velocidad Máxima: 3.40 GHz
  * Numero de núcleos: 4 
  * Humero de hilos: 2
  * Arquitectura: x64
  * Set de instrucciones: Intel® SSE4.1, Intel® SSE4.2, Intel® AVX2
* Tamaño de las cachés del procesador
  * L1: 256 KB
  * L2: 1 MB
  * L3: 6 MB
* Memoria 
  * Total: 4 GB
  * Tipo de memoria:DDR4-2400
  * Velocidad: 2400 MHz
  * Numero de (SO)DIMM: 2
* Tarjeta Gráfica
  * Marca / Modelo: Intel (R) UHD Graphics 620
  * Memoria dedicada: 1 GB
  * Resolución: 1920 x 1080 x 60 hercios
* Disco 1: 
  * Marca: Intel Optane
  * Tipo: HDD
  * Tamaño: 932GB
  * Particiones: 3
  * Sistema de archivos: NTFS

  
* Dirección MAC de la tarjeta wifi: F8:A2:D6:E2:A9:41 
* Dirección IP (Interna, del router): 192.168.0.9
* Dirección IP (Externa, del ISP): 190.160.0.13
* Proveedor internet: VTR Banda Ancha S.A.


* DESEMPEÑO MATMUL
   * ¿Como difiere del gráfico del profesor? Difiere bastante en el tiempo de ejecución de cada corrida y levemente en la memoria utilizada.
   * ¿ A que se pueden deber estas diferencias?  Porque cada procesador tiene un distinto intervalo de tiempo en el que un programa se ejecuta en el sistema opertivo. Los rendimientos difieren y por ende un computador tardará mas que otro en ejecutar el código. En este caso el gráfico del profesor muestra que es mas rápido el proceso de ejecución.
   * Tiempo transcurrido no es lineal ¿porque?  De forma automática cada vez que se ejecuta el código se vuelve a realizar todo nuevamente, desde el inicio, tardando una cantidad de tiempo diferente en cada iteración variando en en pocos segundos, con esto el gráfico no se mostrará de forma lineal.
   * Nympy: 1.18.5
   * Versión Python: 3.8
   * Se utiliza solo un procesador. 
