def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    return [row[::-1] for row in matrix]  # Método popular de slicing de listas. El -1 indica que se recorra la lista al revés con un incremento negativo


""" def main():
    print(mirror_matrix([[1, 2, 3], [4, 5, 6]]))


if __name__ == "__main__":
    main() """