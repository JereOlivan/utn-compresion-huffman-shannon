# main.py

from codificacion import *
from utils import *

def elegir_texto():
    # Menú de selección para cargar el string a procesar en memoria
    while True:
        print("\n--- Ingreso de texto ---")
        print("0. Salir del programa")
        print("1. Ingresar texto manualmente")
        print("2. Cargar texto desde archivo (.txt)")
        opcion = input("Seleccione una opción (0, 1 o 2): ")

        if opcion == "0":
            print("\n🚪 Saliendo del programa...")
            exit(0)
        elif opcion == "1":
            texto = input("Ingrese el texto: ")
            if texto.strip() == "":
                print("⚠️ El texto no puede estar vacío.")
                continue
            return texto
        elif opcion == "2":
            while True:
                ruta = input("Ingrese la ruta del archivo (o '0' para volver): ")
                if ruta == "0":
                    break
                texto = leer_texto(ruta)
                if texto is not None:
                    return texto
                print("❌ Ruta inválida. Intentá nuevamente.")
        else:
            print("❌ Opción inválida.")

def comparar_algoritmos(texto):
    # Validación de seguridad: no se puede comprimir un texto con un solo carácter repetido
    if len(set(texto)) < 2:
        print("⚠️ El texto debe contener al menos 2 símbolos distintos.")
        return

    # Se calculan métricas de línea base teóricas
    probs = calcular_probabilidades(texto)
    entropia = calcular_entropia(probs)

    print("\n📊 Comparación de algoritmos:\n")

    resultados = []

    # Procesa la codificación, decodificación y métricas mediante HUFFMAN
    cod_h, codificado_h, arbol_h = huffman_codificar(texto)
    decodificado_h = huffman_decodificar(codificado_h, cod_h)
    l_prom_h = calcular_longitud_promedio(probs, cod_h)
    eficiencia_h = calcular_eficiencia(entropia, l_prom_h)

    resultados.append(("Huffman", cod_h, codificado_h, entropia, l_prom_h, eficiencia_h, decodificado_h))

    # Procesa la codificación, decodificación y métricas mediante SHANNON-FANO
    cod_sf, codificado_sf = shannon_fano_codificar(texto)
    decodificado_sf = shannon_fano_decodificar(codificado_sf, cod_sf)
    l_prom_sf = calcular_longitud_promedio(probs, cod_sf)
    eficiencia_sf = calcular_eficiencia(entropia, l_prom_sf)

    resultados.append(("Shannon-Fano", cod_sf, codificado_sf, entropia, l_prom_sf, eficiencia_sf, decodificado_sf))

    # Imprime en consola todos los resultados para comparativa (sin renderización gráfica aún)
    for nombre, codigos, codificado, H, L, E, decodificado in resultados:
        tasa = calcular_tasa_compresion(texto, codificado)

        print(f"🔎 {nombre}")
        mostrar_tabla_codigos(codigos)
        print(f"📏 Longitud promedio: {L:.4f}")
        print(f"📈 Entropía (H): {H:.4f}")
        print(f"📊 Eficiencia: {(E * 100):.2f}%")
        print(f"📉 Tasa de compresión: {tasa:.2f}")
        print(f"🔒 Codificado: {codificado}")
        print(f"🔓 Decodificado: {decodificado}")
        print(f"✔ Decodificación correcta: {decodificado == texto}\n")

def menu():
    # Bucle principal de inicio de sistema
    while True:
        limpiar_pantalla()
        print("===================================")
        print("  COMPRESIÓN CON HUFFMAN Y SHANNON")
        print("  ESTADO: EN DESARROLLO")
        print("===================================")

        texto = elegir_texto()
        comparar_algoritmos(texto)

        repetir = input("\n¿Deseás analizar otro texto? (s/n): ").lower()
        if repetir != "s":
            print("\nGracias por usar el codificador.")
            break

if __name__ == "__main__":
    menu()