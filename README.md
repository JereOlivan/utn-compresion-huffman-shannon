# utn-compresion-huffman-shannon
Implementación y análisis comparativo de algoritmos de compresión de datos (Huffman y Shannon-Fano) en Python. Proyecto en desarrollo.

IMPORTANTE: PARA INICIAR EJECUTABLE DEBE TENER PYTHON INSTALADO EN TU PC

# 📊 Compresión de Datos: Huffman vs. Shannon-Fano

## 📝 Descripción
Este proyecto implementa y compara dos de los algoritmos clásicos de la Teoría de la Información para la compresión de datos sin pérdida: **Huffman** (Bottom-Up) y **Shannon-Fano** (Top-Down). 

El sistema toma una cadena de texto, calcula sus métricas teóricas fundamentales (probabilidades y Entropía de Shannon) y genera los códigos binarios óptimos para cada carácter, permitiendo evaluar la eficiencia y la tasa de compresión de ambos enfoques.

## ⚙️ Arquitectura del Proyecto
El código está modularizado en tres archivos principales para separar la lógica matemática de la interfaz de usuario:
* `main.py`: Punto de entrada del programa y menú interactivo.
* `codificacion.py`: Contiene las estructuras de datos (como el árbol de Huffman) y la lógica recursiva de los algoritmos.
* `utils.py`: Herramientas matemáticas para el cálculo de entropía, longitud promedio y métricas de rendimiento.

## 🚧 Estado del Proyecto: En Desarrollo (WIP)
Actualmente, el motor matemático y lógico de ambos algoritmos es 100% funcional en la consola de comandos. El sistema codifica, decodifica y valida la integridad de los datos correctamente.

**Próximo Sprint:**
* Integración de librerías de visualización de datos.
* Renderizado gráfico del árbol binario de Huffman.
* Gráficos comparativos de longitud de códigos.
