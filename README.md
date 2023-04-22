# Ejemplo de MT

Vamos a construir usando la biblioteca automata la MT que decide el lenguaje:

```
Sea Σ = { a },
L = { w#w | w ∈ Σ* }
```

## Instrucciones

Crear un entorno virtual o abrir con un IDE que soporte entornos virtuales.

Instalar las librerías del archivo requirements.txt.

### Usar desde consola del SO

```bash
python iguales.py
```

Tipeamos las cadenas y luego de apretar enter imprime ACEPTA o RECHAZA.

Podemos usar con un archivo con un conjunto de casos:

```bash
python iguales.py < casos.txt
```

Si nos gustaría ver paso a paso lo que pasa con todas las configuraciones y el historial de computo completo:

```bash
python iguales.py --debug
```

### Usar desde consola de python

```python
import iguales

iguales.evaluar('aa#aa')
```

Devuelve True cuando acepta y False cuando rechaza.

Para poder observar el historial de cómputo, llamar a evaluar con True en el segundo parámetro:

```python
import iguales

iguales.evaluar('aa#aa', True)
```

### Probar con pytest

pytest es una biblioteca de python que nos permite ejecutar pruebas.

Desde el entorno virtual ejectuar:

```
python -m pytest
```