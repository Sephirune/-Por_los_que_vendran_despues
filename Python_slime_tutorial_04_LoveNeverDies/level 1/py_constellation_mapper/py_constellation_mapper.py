"""
SUBJECT
-------
Implementa la funcion constellation_mapper. La funcion debe:
- Tomar una lista de tuplas, cada una con un entero (fila) y un entero (columna).
- Devolver una lista de cadenas (list[str]) que represente una cuadricula
  de tamano size x size, compuesta por "." y "*" segun las coordenadas
  proporcionadas en stars.
- Ignorar las coordenadas fuera de los limites de la cuadricula.
- Ignorar las coordenadas duplicadas.

Firma:
    def constellation_mapper(stars: list[tuple[int, int]], size: int) -> list[str]:

Ejemplos:
    constellation_mapper([(0, 0), (1, 1), (2, 2)], 3)                 -> ["*..", ".*.", "..*"]
    constellation_mapper([(0, 0), (0, 1), (0, 2), (1, 1), (2, 2)], 3) -> ["***", ".*.", "..*"]
    constellation_mapper([(0, 0), (5, 5), (2, 2)], 3)                 -> ["*..", "...", "..*"]
    constellation_mapper([(0, 0), (5, 5)], 2)                         -> ["*.", ".."]
"""


def constellation_mapper(stars: list[tuple[int, int]], size: int) -> list[str]:
    # Cuadricula de listas para poder modificar posiciones
    grid = [['.'] * size for _ in range(size)]

    for row, col in stars:
        if 0 <= row < size and 0 <= col < size:
            grid[row][col] = '*'  # los duplicados simplemente reescriben '*'

    return [''.join(row) for row in grid]


""" def main():
    print(constellation_mapper([(0, 0), (1, 1), (2, 2)], 3))
    print(constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3))
    print(constellation_mapper([(0, 0), (5, 5), (2, 2)], 3))
    print(constellation_mapper([(0, 0), (5, 5)], 3))


if __name__ == "__main__":
    main()
 """