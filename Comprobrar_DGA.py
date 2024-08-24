import argparse, math, csv, re
from collections import Counter

def extraer_nombre_dominio(dominio):
    patron = r'^(?:https?://)?(?:www\.)?([^/]+?)(?:\.[a-z]{2,8})?$'
    resultado = re.search(patron, dominio)
    if resultado:
        return resultado.group(1)
    return None

def calcular_entropia(dominio):

    frecuencia = Counter(dominio)
    longitud = len(dominio)
    
    entropia = -sum((frecuencia[caracter] / longitud) * math.log2(frecuencia[caracter] / longitud) for caracter in frecuencia)
    return entropia

def calcular_frecuencia(dominio):

    coeficientes = {
        '0': 0.0024875471880163543,
        '1': 0.004884638114650296,
        '2': 0.004373560237839663,
        '3': 0.0021136613076357144,
        '4': 0.001625197496170685,
        '5': 0.0013070929769758662,
        '6': 0.0014880054997406921,
        '7': 0.001471421851820583,
        '8': 0.0012663876593537805,
        '9': 0.0010327089841158806,
        'a': 0.0733359063114348,
        'b': 0.0429320492564495,
        'c': 0.0273856331335255,
        'd': 0.027694692026582,
        'e': 0.0708619275626258,
        'f': 0.0124965325099803,
        'g': 0.0385162760966314,
        'h': 0.0240176450013869,
        'i': 0.0604473966687974,
        'j': 0.00708272526624292,
        'k': 0.01659570875496,
        'l': 0.0581588532558223,
        'm': 0.0338849155138518,
        'n': 0.0475317501477452,
        'o': 0.094137831220677,
        'p': 0.0425551481673561,
        'q': 0.00172319177933496,
        'r': 0.0646008466706065,
        's': 0.0721464064742561,
        't': 0.0644772231133839,
        'u': 0.0347924933363887,
        'v': 0.0116371980268474,
        'w': 0.0133181768842039,
        'x': 0.00317049196145357,
        'y': 0.0163816289363549,
        'z': 0.00471578642673645
    }
    
    frecuencias = {}
    for char in dominio:
        if char in frecuencias:
            frecuencias[char] += 1
        else:
            frecuencias[char] = 1
    
    resultado = sum(frecuencias[char] * coef for char, coef in coeficientes.items() if char in frecuencias)
    
    return round(resultado, 2)

def Comprobar(dominio):

    DGA = False
    longitud = len(dominio)
    entropia = calcular_entropia(dominio)
    frecuencia = calcular_frecuencia(dominio)

    if longitud == 5:
        if (0.05 <= frecuencia <= 0.23) and (1.9 <= entropia <= 2.32195):
            DGA = True
    elif longitud == 6:
        if (0.05 <= frecuencia <= 0.29) and (1.45 <= entropia <= 2.59):
            DGA = True
    elif longitud == 7:
        if (0.15 <= frecuencia <= 0.32) and (1.65 <= entropia <= 2.81):
            DGA = True
    elif longitud == 8:
        if (0.15 <= frecuencia <= 0.37) and (2.40 <= entropia <= 3.00):
            DGA = True
    elif longitud == 9:
        if (0.15 <= frecuencia <= 0.45) and (2.00 <= entropia <= 3.15):
            DGA = True
    elif longitud == 10:
        if (0.27 <= frecuencia <= 0.50) and (2.40 <= entropia <= 3.20):
            DGA = True
    elif longitud == 11:
        if (0.06 <= frecuencia <= 0.57) and (3 <= entropia <= 3.47):
            DGA = True
    elif longitud == 12:
        if (0.22 <= frecuencia <= 0.62) and (2.65 <= entropia <= 3.50):
            DGA = True
    elif longitud == 13:
        if (0.2 <= frecuencia <= 0.60) and (2.40 <= entropia <= 3.60):
            DGA = True
    elif longitud == 14:
        if (0.2 <= frecuencia <= 0.75) and (2.4 <= entropia <= 3.50):
            DGA = True
    elif longitud == 15:
        if (0.30 <= frecuencia <= 0.80) and (2.90 <= entropia <= 3.70):
            DGA = True
    elif longitud == 16:
        if (0.40 <= frecuencia <= 0.80) and (3.00 <= entropia <= 4.00):
            DGA = True
    elif longitud == 17:
        if (0.40 <= frecuencia <= 0.85) and (3.00 <= entropia <= 3.80):
            DGA = True
    elif longitud == 18:
        if (0.50 <= frecuencia <= 0.90) and (3.25 <= entropia <= 3.90):
            DGA = True
    elif longitud == 19:
        if (0.5 <= frecuencia <= 1) and (3.40 <= entropia <= 4.00):
            DGA = True
    elif longitud == 20:
        if (0.5 <= frecuencia <= 1) and (3.50 <= entropia <= 4.10):
            DGA = True
    elif longitud == 21:
        if (0.5 <= frecuencia <= 1.02) and (3 <= entropia <= 4.00):
            DGA = True
    elif longitud == 22:
        if (0.6 <= frecuencia <= 1.10) and (3.52 <= entropia <= 4.20):
            DGA = True
    elif longitud == 23:
        if (0.5 <= frecuencia <= 1.15) and (3.50 <= entropia <= 4.20):
            DGA = True
    elif longitud == 24:
        if (0.30 <= frecuencia <= 1.20) and (3.50 <= entropia <= 4.30):
            DGA = True
    elif longitud == 25:
        if (0.40 <= frecuencia <= 1.2) and (3.50 <= entropia <= 4.40):
            DGA = True
    elif longitud == 26:
        if (0.35 <= frecuencia <= 1.41) and (3.50 <= entropia <= 4.50):
            DGA = True
    elif longitud == 27:
        if (0.4 <= frecuencia <= 0.9) and (3.60 <= entropia <= 4.40):
            DGA = True
    elif longitud == 28:
        if (0.4 <= frecuencia <= 1) and (3.75 <= entropia <= 4.40):
            DGA = True
    else:
        print("Dominio con longitud no valida")
    
    if DGA == True:
        print(f"El dominio {dominio} es un DGA")
    else:
        print(f"El dominio {dominio} no es un DGA")

def main():
    parser = argparse.ArgumentParser(description='Programa para discriminar un DGA de un No-DGA')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-dominio', '-d', type=str, help='Dominio para analizar')
    group.add_argument('-lista', '-l', type=str, help='Archivo CSV con una lista de dominios')

    args = parser.parse_args()

    if args.dominio:
        dominio = extraer_nombre_dominio(args.dominio)
        Comprobar(dominio)

    elif args.lista:
        with open(args.lista, mode='r', newline='') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            for fila in lector_csv:
                for valor in fila:
                    dominio = extraer_nombre_dominio(valor)
                    Comprobar(dominio)

if __name__ == "__main__":
    main()
