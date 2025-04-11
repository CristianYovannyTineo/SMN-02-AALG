#Supóngase que en una reciente elección hubo cuatro candidatos, con identificadores 1, 2, 3, 4. 
# Usted habrá de encontrar mediante un programa, el número de votos correspondiente a cada candidato y el porcentaje que obtuvo respecto al total de los votantes.
#  El usuario ingresara los votos de manera desorganizada, tal y como se obtuvieron en la elección, el final de datos está representado por un cero.
#Observe, como ejemplo, la siguiente lista.: 1 3 1 4 2 2 1 3 1 1 1 3 4 1 2 4 4 0

#Integrantes:
#Espinoza Rios Pedro Manuel, N00370898
#Eduardo Wilfredo Sabroso Abanto, N00367926
#Gian Franco David Cardenas Arroyo, N00358216
#Tineo Labio Cristian Yovanny, N00378004
#Oscar Andre Olano Cauchos, N00368755


def contar_votos():
    print("Ingresa los votos (usa espacio entre ellos, termina con 0):")
    entrada = input()
    votos = list(map(int, entrada.strip().split()))

    # Eliminar el 0 final
    if votos[-1] == 0:
        votos.pop()

    # Inicializar contadores
    conteo = {1: 0, 2: 0, 3: 0, 4: 0}
    total_votos = 0

    for voto in votos:
        if voto in conteo:
            conteo[voto] += 1
            total_votos += 1
        else:
            print(f"Voto inválido ignorado: {voto}")

    print("\nResultados:")
    for candidato in range(1, 5):
        porcentaje = (conteo[candidato] / total_votos * 100) if total_votos > 0 else 0
        print(f"Candidato {candidato}: {conteo[candidato]} votos ({porcentaje:.2f}%)")

# Ejecutar la función
contar_votos()
