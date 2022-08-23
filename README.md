# Circuitpython Reave

Cosplay de Reave Maeve usando CircuitPython

## Hardware

Utiliza una Qt con chip ESP32-C3, la cual se controla por medio de Web Api.

Nota: Necesita versión "newest" mientras sale un release alpha para la C3.

Se controlan varias tiras de Neopixeles para dibujar varios patrones de caras de Reave.

## Software

- [x] Se utiliza CircuitPython para control sencillo de las tiras de neopixeles
- [x] Existe una función de espejo, que permite definir los pixeles de solo un lado de la cara y con el espejo se muestra el otro lado
- [ ] Funcion de animaciones, que traen los patrones de variables y los muestran en la tira
- [ ] Código para tarjeta controladora y tarjeta escucha, para poder coordinar la C3 del casco (controladora) y del traje+botas (escucha)
- [ ] Código que imprime en texto el patrón a dibujar según variable DEBUG=1 al iniciar el código, para verificar desde web REPL
- [x] Funciones en archivo para importar, y patrones en archivo para importar, para mejorar el comportamiento de depurado en web REPL

## Matrix de patrones

La matrix se define de forma que utiliza pixeles definidos en 2 para prendido/apagado en el color seleccionado, 0 para apagado (0,0,0), y opcionalmente 1 para prendido con color pero a menor intensidad y de ser necesario, 3 para el color pero en mayor intensidad.

Existe una complejidad adicional, y es que por la forma de como están configuradas las PCBs en los módulos de 2x2 y 4x4, se deben dibujar al revez las filas 2 y 4.

# 4x4
ojo_iz = [ 1, 1, 0, 0,
           0, 1, 1, 0,
           0, 1, 1, 0,
           0, 0, 0, 1 ]
