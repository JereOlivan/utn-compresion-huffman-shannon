# utils.py

import os
import math
from collections import Counter

def limpiar_pantalla():
    # Limpia la consola de comandos dependiendo del sistema operativo (Windows 'nt' o Mac/Linux 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')

def leer_texto(ruta):
    # Intenta abrir y leer un archivo txt usando la ruta proporcionada.
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read()
            # Retorna el contenido solo si el texto no está vacío o compuesto de puros espacios
            return contenido if contenido.strip() else None
    except:
        return None

def mostrar_tabla_codigos(codigos):
    # Recorre el diccionario de códigos generados e imprime cada símbolo con su representación en binario
    print("Símbolo\tCódigo")
    for simbolo, codigo in sorted(codigos.items()):
        print(f"{repr(simbolo)}\t{codigo}")
    print()

def calcular_probabilidades(texto):
    # Cuenta las apariciones de cada carácter y las divide por el total de caracteres para obtener su probabilidad
    total = len(texto)
    return {c: f / total for c, f in Counter(texto).items()}

def calcular_entropia(probs):
    # Aplica la fórmula matemática de la entropía de Shannon (sumatoria de p * log2(p) negativo)
    # Sirve como límite teórico de compresión máxima
    return -sum(p * math.log2(p) for p in probs.values())

def calcular_longitud_promedio(probs, codigos):
    # Multiplica la probabilidad de cada símbolo por la cantidad de bits que usa su nuevo código
    return sum(probs[s] * len(codigos[s]) for s in probs)

def calcular_eficiencia(H, L):
    # Compara la entropía (H) ideal contra la longitud promedio (L) que logramos con el algoritmo
    return H / L if L != 0 else 0

def calcular_tasa_compresion(texto_original, texto_codificado):
    # Calcula el peso del texto en ASCII estándar (8 bits por letra) versus los bits de nuestra cadena codificada
    bits_original = len(texto_original) * 8  
    bits_codificado = len(texto_codificado)  
    if bits_codificado == 0:
        return 0
    return bits_original / bits_codificado