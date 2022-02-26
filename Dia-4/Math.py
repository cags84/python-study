# Math
# El homologo de switch

serie = "N-02"

if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print("No existe ese producto")

# Ahora con Match
serie = "N-02"

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe ese producto")

cliente = {
    'nombre': 'federico',
    'edad': 45,
    'ocupacion': 'instructor'
}

pelicula = {
    'titulo': 'Matrix',
    'ficha_tecnica': {
        'protagonista': 'Keanu Reeves',
        'director': 'Lana y Lilly Wachoski'
    }
}

elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {
            'nombre': nombre,
            'edad': edad,
            'ocupacion': ocupacion
        }:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case {
            'titulo': titulo,
            'ficha_tecnica': {
                'protagonista': protagonista,
                'director': director
            }
        }:
            print("Esto es una pelicula")
            print(titulo, protagonista, director)
        case _:
            print("No se que es esto")
