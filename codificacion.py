# codificacion.py

from collections import Counter
import heapq

# --- ALGORITMO DE HUFFMAN ---

class NodoHuffman:
    def __init__(self, simbolo, frecuencia):
        # Cada nodo guarda un símbolo de texto y su frecuencia de aparición. 
        # Si es un nodo "padre", el símbolo será None.
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        # Sobrescribe el operador "menor que" para que la cola de prioridad (heap) ordene por frecuencia
        return self.frecuencia < otro.frecuencia

def construir_arbol_huffman(texto):
    # Transforma las letras y frecuencias en Nodos, y los ordena de menor a mayor en un heap
    heap = [NodoHuffman(s, f) for s, f in Counter(texto).items()]
    heapq.heapify(heap)

    # Mientras haya más de 1 nodo, saca los 2 más chicos, los suma en un nodo padre y lo devuelve al heap
    while len(heap) > 1:
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)
        nuevo = NodoHuffman(None, n1.frecuencia + n2.frecuencia)
        nuevo.izquierda = n1
        nuevo.derecha = n2
        heapq.heappush(heap, nuevo)

    # Retorna la raíz del árbol completado
    return heap[0]

def generar_codigos_huffman(nodo, prefijo="", codigos=None):
    # Recorre el árbol recursivamente: viaja a la izquierda agregando "0", o a la derecha agregando "1"
    if codigos is None:
        codigos = {}

    if nodo.simbolo is not None:
        # Si encuentra un símbolo hoja, guarda el "camino" binario acumulado
        codigos[nodo.simbolo] = prefijo or "0"
        return codigos

    generar_codigos_huffman(nodo.izquierda, prefijo + "0", codigos)
    generar_codigos_huffman(nodo.derecha, prefijo + "1", codigos)

    return codigos

def huffman_codificar(texto):
    # Orquesta el proceso: arma el árbol, genera el diccionario y reemplaza cada letra por su código final
    arbol = construir_arbol_huffman(texto)
    codigos = generar_codigos_huffman(arbol)
    codificado = ''.join(codigos[c] for c in texto)
    return codigos, codificado, arbol

def huffman_decodificar(codificado, codigos):
    # Invierte el diccionario (Código -> Símbolo) y lee los bits uno a uno hasta hacer "match"
    inv = {v: k for k, v in codigos.items()}
    actual = ""
    decodificado = ""
    for bit in codificado:
        actual += bit
        if actual in inv:
            decodificado += inv[actual]
            actual = ""
    return decodificado

# --- ALGORITMO DE SHANNON-FANO ---

def calcular_frecuencias(texto):
    # Genera una lista de tuplas (símbolo, probabilidad) ordenada de mayor a menor aparición
    total = len(texto)
    freqs = Counter(texto)
    return sorted([(s, f / total) for s, f in freqs.items()], key=lambda x: -x[1])

def asignar_codigos_shannon(simbolos, codigos, prefijo=""):
    # Condición de corte recursivo: si queda 1 solo elemento, se le asigna el código que armó
    if len(simbolos) == 1:
        codigos[simbolos[0][0]] = prefijo or "0"
        return

    # Busca el punto de corte para dividir la lista en dos partes con probabilidades lo más parejas posible
    total = sum(f for _, f in simbolos)
    acc = 0
    for i in range(len(simbolos)):
        acc += simbolos[i][1]
        if acc >= total / 2:
            break

    # Divide las listas y repite la lógica: '0' a la mitad superior, '1' a la inferior
    izquierda = simbolos[:i+1]
    derecha = simbolos[i+1:]
    asignar_codigos_shannon(izquierda, codigos, prefijo + "0")
    asignar_codigos_shannon(derecha, codigos, prefijo + "1")

def shannon_fano_codificar(texto):
    # Centraliza el flujo para calcular, asignar los códigos top-down y armar el texto final binario
    simbolos = calcular_frecuencias(texto)
    codigos = {}
    asignar_codigos_shannon(simbolos, codigos)
    codificado = ''.join(codigos[c] for c in texto)
    return codigos, codificado

def shannon_fano_decodificar(codificado, codigos):
    # Funciona igual que en Huffman: diccionario invertido e iteración bit por bit
    inv = {v: k for k, v in codigos.items()}
    actual = ""
    decodificado = ""
    for bit in codificado:
        actual += bit
        if actual in inv:
            decodificado += inv[actual]
            actual = ""
    return decodificado