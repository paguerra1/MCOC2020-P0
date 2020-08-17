# Entrega 6
# Desempeño Ax=b (Parte 2)
![PAULINA GUERRA_Gráfico Ax=b(parte 2)](https://user-images.githubusercontent.com/69210578/90343112-9c387900-dfdb-11ea-9d73-6d0a08aa321f.png)
* Mejor desempeño:
  * Según lo mostrado en el gráfico, se pueden analizar distintas aristas. En primer lugar se ve como en un comienzo, para las matrices mas pequeñas hasta las matrices de 50x50 el que muestra un mejor desempeño es "A_invB_npSolve" de Numpy, superando por poco 0.1 ms. Pero desde las matrices de 50x50 hasta las matrices mas grandes es "A_invB_spSolve_pos_overwrite", solver de scipy que resuelve de forma mas rápida Ax=b,demorándose 8seg aprox. para las matrices de 10.000x10.000.  Esto demuestra que cuando se sabe que la matriz es definida positiva, el algoritmo es mas eficiente, para esto se escribe: "assume_a='pos'". 
  * Quedó demostrado que mayor es la eficiencia cuando se agrega "overwrite_a" donde permite sobre escribir los datos. Eficiencia ya demostrada previamente en la entrega anterior.
  
* Peor desempeño:
  * Con respecto a las funciones mas lentas o menos eficientes, destaca "A_invB_inv", donde se invierte la matriz A y luego se multiplica por el vector B de unos. Es una función claramente menos eficiente en comparación a las demas, ya que es mas larga, tediosa y no inmediatamente directa. Esta función es la que presenta mas tiempo en todos los casos, para matrices de 10.000x10.000 se demora casi 1 min. 
  * Pero en solo algunas partes la función "A_invB_spSolve_symmetric" supera en tiempo de demora a la función previamente comentada. Esto ocurre para las matrices mas pequeñas que se demora 80ms aproximadamente mientras que las demás funciones no superan los 3 ms. Luego tiene otro aumento para las matrices de 100x100 explicandose por un posible uso de otro programa de forma paralela a la ejecución del código. Para esta función el programa asume que la matriz es simétrica, lo que implica que los valores sobre y bajo la diagonal son los mismos. La función solve permite establecer el argumento "assume_a='sym'".
  * La segunda función mas lenta es  "A_invB_spSolve" durante casi todo el gráfico.
    
* Conclusión desempeño, orden de mejor a peor rendimiento:
  * 1º spSolve_pos_overwrite
  * 2º spSolve_pos
  * 3º npSolve
  * 4º spSolve_symetric
  * 5º spSolve
  * 6º Invertir y multiplicar
  
* El orden de rendimiento por función coincide con el del gráfico del profesor, pero ese muestra menos tiempo en la ejecución. Para la función "A_invB_inv" se demoró 20 seg. aproximadamente para las matrices de 10.000x10.000 mientras que en mi computador esta misma función demoró casi un minuto para el mismo tamaño de matrices. Lo que previamente se ha explicado por la diferencia de procesadores, memoria RAM y paralelismo en cada ordenador, siendo el computador del profesor mas eficiente que el mio.
* Ambos gráficos muestran que cuando se asume que la matriz es simétrica, esta función demora mas de lo habitual justo al comenzar para las matrices mas pequeñas de 2x2 o 4x4 (función representada en rojo)
